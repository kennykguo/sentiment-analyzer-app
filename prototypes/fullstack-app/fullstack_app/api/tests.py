from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework import status
from .models import Company, Sentiment, Statistics

class APITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.registration_url = '/api/register/'
        self.token_url = '/api/token/'
        self.company_url = '/api/company/'
        self.sentiments_url = '/api/sentiments/'
        self.statistics_url = '/api/statistics/'

    def test_registration(self):
        data = {
            'username': 'testuser',
            'email': 'testuser@example.com',
            'password': 'testpassword',
            'company_name': 'Test Company'
        }
        response = self.client.post(self.registration_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(User.objects.filter(email='testuser@example.com').exists())

    def test_token_obtain(self):
        # First, create a user
        user = User.objects.create_user(username='testuser', email='testuser@example.com', password='testpassword')
        Company.objects.create(user=user, name='Test Company')

        data = {
            'email': 'testuser@example.com',
            'password': 'testpassword'
        }
        response = self.client.post(self.token_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('access', response.data)
        self.assertIn('refresh', response.data)

    def test_company_data(self):
        # Create a user and get token
        user = User.objects.create_user(username='testuser', email='testuser@example.com', password='testpassword')
        company = Company.objects.create(user=user, name='Test Company')
        response = self.client.post(self.token_url, {'email': 'testuser@example.com', 'password': 'testpassword'}, format='json')
        token = response.data['access']

        # Test company data endpoint
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')
        response = self.client.get(self.company_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Test Company')

    def test_sentiments(self):
        # Create a user, company, and sentiments
        user = User.objects.create_user(username='testuser', email='testuser@example.com', password='testpassword')
        company = Company.objects.create(user=user, name='Test Company')
        Sentiment.objects.create(company=company, review="Good service")
        Sentiment.objects.create(company=company, review="Could be better")

        # Get token and set credentials
        response = self.client.post(self.token_url, {'email': 'testuser@example.com', 'password': 'testpassword'}, format='json')
        token = response.data['access']
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')

        # Test sentiments endpoint
        response = self.client.get(self.sentiments_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_statistics(self):
        # Create a user, company, and statistics
        user = User.objects.create_user(username='testuser', email='testuser@example.com', password='testpassword')
        company = Company.objects.create(user=user, name='Test Company')
        Statistics.objects.create(company=company, mean=4.5, standard_deviation=0.5)

        # Get token and set credentials
        response = self.client.post(self.token_url, {'email': 'testuser@example.com', 'password': 'testpassword'}, format='json')
        token = response.data['access']
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')

        # Test statistics endpoint
        response = self.client.get(self.statistics_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['mean'], 4.5)
        self.assertEqual(response.data['standard_deviation'], 0.5)