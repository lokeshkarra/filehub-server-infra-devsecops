from django.test import TestCase
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient
from rest_framework import status
from django.core.files.uploadedfile import SimpleUploadedFile
from .models import File
User = get_user_model()
class FileUploadTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpassword123'
        )
        self.client.force_authenticate(user=self.user)
        # Create a test file
        self.test_file = SimpleUploadedFile(
            name='test_file.txt',
            content=b'This is a test file content',
            content_type='text/plain'
        )
    def test_file_upload(self):
        response = self.client.post('/api/files/',
                                     {'file': self.test_file},
                                     format='multipart'
                                     )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(File.objects.filter(owner=self.user).exists())

    def test_file_list(self):
        # Upload a file first
        self.client.post('/api/files/',
                         {'file': self.test_file},
                         format='multipart'
                         )
        # List files
        response = self.client.get('/api/files/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(len(response.data) > 0)

    def test_file_delete(self):
        # Upload a file first
        upload_response = self.client.post('/api/files/',
                                            {'file': self.test_file},
                                            format='multipart'
                                            )
        file_id = upload_response.data['id']
        # Delete the file
        delete_response = self.client.delete(f'/api/files/{file_id}/')
        self.assertEqual(delete_response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(File.objects.filter(id=file_id).exists())