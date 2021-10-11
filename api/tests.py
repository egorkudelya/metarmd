from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from . import models

# Create your tests here.
class ContextTests(APITestCase):


    def test_create_context(self):

        url = 'http://127.0.0.1:8000/contexts/'
        data = {'name': 'KA-02'}
        response = self.client.post(url, data, format='json')
        # data = response.data
        # data1 = json.loads(data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(models.Context.objects.count(), 1)
        self.assertEqual(models.Context.objects.get().name, 'KA-02')


    def test_create_subject(self):

        url = 'http://127.0.0.1:8000/contexts/'
        data = {'name': 'KA-03'}
        response = self.client.post(url, data, format='json')
        context_id = str(response.data['id'])

        data = {'name': 'OOP'}
        url = url + context_id + '/subjects/'
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(models.Subject.objects.count(), 1)
        self.assertEqual(models.Subject.objects.get().name, 'OOP')



