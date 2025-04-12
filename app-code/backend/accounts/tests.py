# from django.test import TestCase
# from django.contrib.auth import get_user_model
# from rest_framework.test import APIClient
# from rest_framework import status

# User = get_user_model()

# class UserRegistrationTest(TestCase):
#     def setUp(self):
#         self.client = APIClient()
#         self.register_url = '/api/auth/register/'
#         self.login_url = '/api/auth/login/'
#         self.user_data = {
#             'username': 'testuser',
#             'email': 'test@example.com',
#             'password': 'testpassword123',
#             'confirm_password': 'testpassword123'
#         }

#     def test_user_registration(self):
#         response = self.client.post(self.register_url, self.user_data)
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)
#         self.assertIn('access', response.data)
#         self.assertIn('refresh', response.data)

#     def test_user_login(self):
#         # First register the user
#         self.client.post(self.register_url, self.user_data)
        
#         # Then attempt login
#         login_data = {
#             'email': self.user_data['email'],
#             'password': self.user_data['password']
#         }
#         response = self.client.post(self.login_url, login_data)
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertIn('access', response.data)
#         self.assertIn('refresh', response.data)


# from django.test import TestCase
# from django.contrib.auth import get_user_model
# from rest_framework.test import APIClient
# from rest_framework import status
# User = get_user_model()
# class UserRegistrationTest(TestCase):
#     def setUp(self):
#         self.client = APIClient()
#         self.register_url = '/api/auth/register/'
#         self.login_url = '/api/auth/login/'
#         self.user_data = {
#             'username': 'testuser',
#             'email': 'test@example.com',
#             'password': 'testpassword123',
#             'confirm_password': 'testpassword123'
#         }
#     def test_user_registration(self):
#         response = self.client.post(self.register_url, self.user_data, format='json')
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)
#         self.assertIn('access', response.data)
#         self.assertIn('refresh', response.data)
#     def test_user_login(self):
#         # First register the user
#         self.client.post(self.register_url, self.user_data, format='json')
#         # Then attempt login
#         login_data = {
#             'username': self.user_data['username'],  # Use username instead of email
#             'password': self.user_data['password'],
#         }
#         response = self.client.post(self.login_url, login_data, format='json')
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertIn('access', response.data)
#         self.assertIn('refresh', response.data)

        
from django.test import TestCase
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient
from rest_framework import status

User = get_user_model()
class UserRegistrationTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.register_url = '/api/auth/register/'
        self.login_url = '/api/auth/login/'
        self.user_data = {
            'username': 'testuser',
            'email': 'test@example.com',
            'password': 'testpassword123',
            'confirm_password': 'testpassword123'
        }
    def test_user_registration(self):
        response = self.client.post(self.register_url, self.user_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        # Assert that access and refresh tokens are present in the response
        self.assertIn('access', response.data)
        self.assertIn('refresh', response.data)

    def test_user_login(self):
        # First register the user
        self.client.post(self.register_url, self.user_data, format='json')

        # Then attempt login
        login_data = {
            'username': 'testuser',
            'password': 'testpassword123',
        }
        response = self.client.post(self.login_url, login_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Assert that access and refresh tokens are present in the response
        self.assertIn('access', response.data)
        self.assertIn('refresh', response.data)