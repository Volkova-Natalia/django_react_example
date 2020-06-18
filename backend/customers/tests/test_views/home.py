from django.test import TestCase
from django.test.client import Client
from rest_framework import status
from django.shortcuts import render


# Create your tests here.
class HomeTestCase(TestCase):
    url = ''

    @classmethod
    def setUpTestData(cls):
        pass

    def setUp(self):
        pass

    def tearDown(self):
        pass

    # ======================================================================

    def test_get(self):
        client = Client()
        response = client.get(self.url)
        self.assertEquals(response.status_code, status.HTTP_200_OK)

        request = response.context['request']
        response_content_expected = render(request, 'customers/_home.html').content
        self.assertEquals(response.content, response_content_expected)

    # ======================================================================
