from django.conf import settings
from django.core.files import File
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status

from documents.models import Document


class DocumentsTests(APITestCase):

    def tearDown(self):
        for f in Document.objects.all():
            f.delete()

    def test_post(self):
        url = reverse('documents-list')
        path = 'documents/tests/files/test_upload_00.txt'
        f = open(path, 'rb')
        data = {'project_file': f,  'title': 'test_upload_00.txt'}
        response = self.client.post(url, data)
        print(response.content)
        f.close()
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(
            response.data['project_file'].startswith(settings.MEDIA_URL))
        self.assertTrue(
            response.data['project_file'].endswith('test_upload_00.txt'))

    def test_put(self):
        document = Document()
        document.title = 'test_upload_v0'
        path = 'documents/tests/files/test_upload_00.txt'
        f = open(path)
        document.project_file.save('test_upload_00.txt', File(f))
        f.close()
        document.save()
        url = reverse('documents-detail', args=['test_upload_v0'])
        path = 'documents/tests/files/test_upload_01.txt'
        f = open(path, 'rb')
        data = {'project_file': f,  'title': 'test_upload_v1'}
        response = self.client.put(url, data)
        f.close()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(
            response.data['project_file'].endswith('test_upload_01.txt'))

    def test_patch(self):
        document = Document()
        document.title = 'test_upload_v0'
        path = 'documents/tests/files/test_upload_00.txt'
        f = open(path)
        document.project_file.save('test_upload_00.txt', File(f))
        f.close()
        document.save()
        url = reverse('documents-detail', args=['test_upload_v0'])
        path = 'documents/tests/files/test_upload_01.txt'
        f = open(path, 'rb')
        data = {'project_file': f}
        response = self.client.patch(url, data)
        f.close()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(
            response.data['project_file'].endswith('test_upload_01.txt'))
