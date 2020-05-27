from django.test import TestCase
from django.test.client import Client
from rest_framework import status

from customers.models import Customer
from django.core.paginator import Paginator
from customers.serializers import CustomerSerializer

import math


# Create your tests here.
def _calc_num_pages(count_customers, count_customers_per_page):
    return math.ceil(count_customers / count_customers_per_page)


class CustomersListTestCase(TestCase):
    url_base = '/api/customers/'
    url_query = url_base + '?page='     # '/api/customers/?page='

    @classmethod
    def setUpTestData(cls):
        pass

    def setUp(self):
        self.count_customers = 126
        self.count_customers_per_page = 10
        # self.num_pages = math.ceil(self.count_customers / self.count_customers_per_page)
        self.num_pages = _calc_num_pages(self.count_customers, self.count_customers_per_page)

        self.test_pages_clear = [page for page in range(1, self.num_pages+1)]
        self.test_pages_dirty = [
            -1,
            0,
            self.num_pages + 1,
            self.num_pages + 2,
        ]
        self.test_pages_all = self.test_pages_clear + self.test_pages_dirty

        self.test_keys = [
            '0',
            '1',
            'value'
        ]

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
        data = paginator.page(page)
        serializer = CustomerSerializer(data, many=True)
        return serializer.data

    def _test_get_clean(self, response, page):
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertEquals(response.data['count_customers'], self.count_customers)
        self.assertEquals(response.data['num_pages'], self.num_pages)
        if page == self.num_pages:
            self.assertEquals(response.data['next_link'], self.url_query + str(1))
        else:
            self.assertEquals(response.data['next_link'], self.url_query + str(page + 1))
        if page == 1:
            self.assertEquals(response.data['prev_link'], self.url_query + str(page))
        else:
            self.assertEquals(response.data['prev_link'], self.url_query + str(page - 1))
        data_expected = self._get_data_expected(page)
        self.assertEquals(response.data['data'], data_expected)

    def test_get_clean(self):
        client = Client()
        response = client.get(self.url_base)
        self._test_get_clean(response, 1)

    def test_get_query_clean(self):
        client = Client()
        for page in self.test_pages_clear:
            response = client.get(self.url_query + str(page))
            self._test_get_clean(response, page)

    # ----- POST -----

    def test_post_clean(self):
        data_post = {
            'first_name': 'first_name_post',
            'last_name': 'last_name_post',
            'email': 'email_post@email.com',
            'phone': 'phone_post',
            'address': '',  # 'address_post',
            'description': '',  # 'description_post',
        }
        client = Client()
        response = client.post(
            path=self.url_base,
            data=data_post,
            content_type='application/json'
        )
        print('\nresponse  ', response)
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)

        count_customers_expected = self.count_customers + 1
        num_pages_expected = _calc_num_pages(count_customers_expected, self.count_customers_per_page)

        count_customers = Customer.objects.count()
        self.assertEquals(count_customers, count_customers_expected)

        customer = Customer.objects.get(id=count_customers)
        for field in data_post.keys():
            self.assertEquals(getattr(customer, field), data_post[field])

        response = client.get(self.url_base)
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertEquals(response.data['count_customers'], count_customers_expected)
        self.assertEquals(response.data['num_pages'], num_pages_expected)

    # ======================================================================
    # dirty
    # ======================================================================

    # ----- GET -----

    def test_get_empty_page_dirty(self):
        client = Client()
        page_expected = self.num_pages
        for page in self.test_pages_dirty:
            response = client.get(self.url_query + str(page))
            self._test_get_clean(response, page_expected)

    def test_get_page_not_an_integer_dirty(self):
        client = Client()
        page_expected = 1
        test_pages = [
            '',
            'first',
        ]
        for page in test_pages:
            response = client.get(self.url_query + str(page))
            self._test_get_clean(response, page_expected)

    def test_get_query_dirty(self):
        client = Client()
        page_expected = 1
        test_queries = ['?'] +\
                       ['?key=' + str(key) for key in self.test_keys] +\
                       ['?page' + str(page) for page in self.test_pages_all] +\
                       ['?page==' + str(page) for page in self.test_pages_all]
        for query in test_queries:
            response = client.get(self.url_base + str(query))
            self._test_get_clean(response, page_expected)

    def test_get_query_missing_dirty(self):
        client = Client()
        test_queries = ['key=' + str(key) for key in self.test_keys] +\
                       ['page=' + str(page) for page in self.test_pages_all]
        for query in test_queries:
            response = client.get(self.url_base + str(query))
            self.assertEquals(response.status_code, status.HTTP_404_NOT_FOUND)

    # ----- POST -----
