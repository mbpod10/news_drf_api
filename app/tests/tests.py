from rest_framework import status
from django.test import TestCase
from news.models import Article
from django.urls import reverse
from rest_framework.test import APIClient
from news.serializers import ArticleSerializer

ARTICLES_URL = reverse('articles:list')


def detail_url(article_id):
    """Return recipe detail URL"""
    return reverse('articles:detail', args=(article_id,))


class ModelTests(TestCase):
    """ Model.full_clean() normalizes datatyptes """

    def setUp(self):
        self.client = APIClient()

    def sample_article(self):
        defaults = {
            'title': "Russia And Ukraine",
            'description': "Breakaway Regions",
            'body': "Leaders of the Russian-led",
            'location': "Moscow",
            'publication_date': "2020-01-19",
            'active': True,
            'author': 'Tito Lance',
            'created_at': '2022-02-19T15:59:41.890730Z',
            'updated_at': '2022-02-19T15:59:41.890730Z',
        }

        return defaults

    def test_create_article_model(self):
        """Test if article create successful"""
        payload = self.sample_article()
        response = self.client.post(ARTICLES_URL, payload)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_article_model_with_same_name_and_description(self):
        """Test title and description cannot be the same"""
        payload = self.sample_article()
        payload['description'] = payload['title']
        response = self.client.post(ARTICLES_URL, payload)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('non_field_errors', response.data)

    def test_article_detail_view(self):
        """Test for the article detail view"""
        payload = self.sample_article()
        article = Article.objects.create(**payload)
        article.full_clean()
        url = detail_url(article.id)
        response = self.client.get(url)
        serializer = ArticleSerializer(article)

        self.assertEqual(response.data, serializer.data)

    def test_article_title_length(self):
        """Test to that title validator has to be more than 10 chars"""
        payload = self.sample_article()
        payload['title'] = 'Not 10'
        response = self.client.post(ARTICLES_URL, payload)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
