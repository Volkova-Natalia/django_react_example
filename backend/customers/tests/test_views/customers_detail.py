from django.test import TestCase
from django.test.client import Client
from rest_framework import status

from customers.models import Customer

import math


# Create your tests here.
def _calc_num_pages(count_customers, count_customers_per_page):
    return math.ceil(count_customers / count_customers_per_page)


class CustomersDetailTestCase(TestCase):
    url_base = '/api/customers/'

    @classmethod
    def setUpTestData(cls):
        pass

    def setUp(self):
        self.count_customers = 126
        self.count_customers_per_page = 10
        self.num_pages = _calc_num_pages(self.count_customers, self.count_customers_per_page)

        self.test_id_customers_clear = [customer for customer in range(1, self.count_customers + 1)]

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

    def test_get_clean(self):
        client = Client()
        for id_customer in self.test_id_customers_clear:
            response = client.get(self.url_base + str(id_customer))
            # self._test_get_clean(response, customer)
            self.assertEquals(response.status_code, status.HTTP_200_OK)

            customer = Customer.objects.get(id=id_customer)
            self.assertEquals(getattr(customer, 'first_name'), 'first_name_' + str(id_customer-1))
            self.assertEquals(getattr(customer, 'last_name'), 'last_name_' + str(id_customer-1))

    # ----- PUT -----

    # ----- DELETE -----

    # ======================================================================
    # dirty
    # ======================================================================

    # ----- GET -----

    # ----- PUT -----

    # ----- DELETE -----
