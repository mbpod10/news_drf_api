from urllib import response
from rest_framework import status
from django.test import TestCase
from news.models import Article
from django.urls import reverse
from rest_framework.test import APIClient

ARTICLES_URL = reverse('articles-list')


class ModelTests(TestCase):

    def setUp(self):
        self.client = APIClient()

    def sample_article(self):
        defaults = {
            'title': "Russia And Ukraine",
            'description': "Breakaway Regions",
            'body': "Leaders of the Russian-led",
            'location': "Moscow",
            'publication_date': '2022-01-19',
            'active': True,
            'created_at': '2022-02-19T15:59:41.890730Z',
            'updated_at': '2022-02-19T15:59:41.890730Z',
        }

        return defaults

    def test_create_article_model(self):
        """Test if article create successful"""
        payload = self.sample_article()
        response = self.client.post(ARTICLES_URL, payload)
        # print(payload)
        # print(response)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_article_model_with_same_name_and_description(self):
        """Test title and description cannot be the same"""

        payload = self.sample_article()
        payload['title'] = "same"
        payload['description'] = "same"
        print(payload)

        response = self.client.post(ARTICLES_URL, payload)
        print(response.data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('non_field_errors', response.data)
