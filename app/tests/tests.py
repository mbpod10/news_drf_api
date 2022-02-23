from rest_framework import status
from django.test import TestCase
from news.models import Journalist
from news.models import Article
from django.urls import reverse
from rest_framework.test import APIClient
from news.serializers import ArticlePostSerializer, ArticleViewSerializer

ARTICLES_URL = reverse('articles:article-list')


def detail_url(article_id):
    """Return recipe detail URL"""
    return reverse('articles:article-detail', args=(article_id,))


def sample_journalist(**params):
    defaults = {
        "first_name": "Amy",
        "last_name": "Suskind",
        "biography": "brief bio"
    }
    defaults.update(params)
    return Journalist.objects.create(**defaults)


def sample_article(author, **params):
    defaults = {
        'title': "Russia And Ukraine",
        'description': "Breakaway Regions",
        'body': "Leaders of the Russian-led",
        'location': "Moscow",
        'publication_date': "2020-01-19",
        'active': True,
    }

    defaults.update(params)
    return Article.objects.create(author=author, **defaults)


class ModelTests(TestCase):
    """ Model.full_clean() normalizes datatyptes """

    def setUp(self):
        self.client = APIClient()
        self.journalist = sample_journalist()
        self.article = sample_article(author=self.journalist)

    def test_create_article_model(self):
        """Test if article create successful"""

        payload = {
            'author': 1,
            'title': "Russia And Ukraine",
            'description': "Breakaway Regions",
            'body': "Leaders of the Russian-led",
            'location': "Moscow",
            'publication_date': "2020-01-19",
            'active': True,
        }

        response = self.client.post(ARTICLES_URL, payload)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_article_model_with_same_name_and_description(self):
        """Test title and description cannot be the same"""
        payload = {
            'author': 1,
            'title': "Russia And Ukraine",
            'description': "Russia And Ukraine",
            'body': "Leaders of the Russian-led",
            'location': "Moscow",
            'publication_date': "2020-01-19",
            'active': True,
        }
        response = self.client.post(ARTICLES_URL, payload)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('non_field_errors', response.data)

    def test_article_detail_view(self):
        """Test for the article detail view"""
        self.article.full_clean()
        url = detail_url(self.article.id)
        response = self.client.get(url)
        serializer = ArticleViewSerializer(self.article)

        self.assertEqual(response.data, serializer.data)

    # def test_article_title_length(self):
    #     """Test to that title validator has to be more than 10 chars"""
    #     # payload = self.sample_article()
    #     # self.article['title'] = 'Not 10'
    #     self.article.update(title="Not Ten")
    #     self.article.save()
    #     response = self.client.put(ARTICLES_URL, self.article)

    #     self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
