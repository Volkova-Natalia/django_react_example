from django.test import TestCase
from django.test.client import Client
from rest_framework import status

from customers.models import Customer
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from customers.serializers import CustomerSerializer

import math


# Create your tests here.
class CustomersListTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        pass

    def setUp(self):
        self.count_customers = 126
        self.count_customers_per_page = 10
        self.num_pages = math.ceil(self.count_customers / self.count_customers_per_page)
        for i in range(self.count_customers):
            Customer(
                first_name='first_name_' + str(i),
                last_name='last_name_' + str(i),
            ).save()

    def tearDown(self):
        pass

    # ======================================================================
    # clean
    # ======================================================================

    # ----- GET -----

    def _get_data_expected(self, page):
        customers = Customer.objects.all()
        paginator = Paginator(customers, self.count_customers_per_page)
        # try:
        #     data = paginator.page(page)
        # except PageNotAnInteger:
        #     data = paginator.page(1)
        # except EmptyPage:
        #     data = paginator.page(paginator.num_pages)
        data = paginator.page(page)
        serializer = CustomerSerializer(data, many=True)
        return serializer.data

    def _test_get_clean(self, response, page):
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertEquals(response.data['count_customers'], self.count_customers)
        self.assertEquals(response.data['num_pages'], self.num_pages)
        if page == self.num_pages:
            self.assertEquals(response.data['next_link'], '/api/customers/?page=' + str(1))
        else:
            self.assertEquals(response.data['next_link'], '/api/customers/?page=' + str(page + 1))
        if page == 1:
            self.assertEquals(response.data['prev_link'], '/api/customers/?page=' + str(page))
        else:
            self.assertEquals(response.data['prev_link'], '/api/customers/?page=' + str(page - 1))
        data_expected = self._get_data_expected(page)
        self.assertEquals(response.data['data'], data_expected)

    def test_get_clean(self):
        client = Client()
        response = client.get('/api/customers/')
        self._test_get_clean(response, 1)

    def test_get_query_clean(self):
        client = Client()
        page = 0
        while page < self.num_pages:
            page = page + 1
            response = client.get('/api/customers/?page=' + str(page))
            self._test_get_clean(response, page)

    # ----- POST -----

    # ======================================================================
    # dirty
    # ======================================================================

    # ----- GET -----

    # ----- POST -----
