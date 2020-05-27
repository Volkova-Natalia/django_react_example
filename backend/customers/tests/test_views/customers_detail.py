from django.test import TestCase
from django.test.client import Client
from rest_framework import status

from customers.models import Customer
from customers.serializers import CustomerSerializer

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
                email='email_' + str(i) + '@email.com',
                phone='phone_' + str(i),
                address='address_' + str(i),
                description='description_' + str(i),
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
            self.assertEquals(getattr(customer, 'email'), 'email_' + str(id_customer-1) + '@email.com')
            self.assertEquals(getattr(customer, 'phone'), 'phone_' + str(id_customer-1))
            self.assertEquals(getattr(customer, 'address'), 'address_' + str(id_customer-1))
            self.assertEquals(getattr(customer, 'description'), 'description_' + str(id_customer-1))

    # ----- PUT -----

    def _test_put_field_clean(self, client, id_customer, field, field_value_new=None):
        customer = Customer.objects.get(id=id_customer)
        data_put = {field: getattr(customer, field) for field in CustomerSerializer.Meta.fields}
        if field_value_new:
            data_put[field] = field_value_new
        else:
            data_put[field] = data_put[field] + '_put'
        # print('\ndata_put', data_put)
        response = client.put(
            path=self.url_base + str(id_customer),
            data=data_put,
            content_type='application/json'
        )
        # print('\nresponse  ', response)
        self.assertEquals(response.status_code, status.HTTP_200_OK)

        customer = Customer.objects.get(id=id_customer)
        for field in CustomerSerializer.Meta.fields:
            self.assertEquals(getattr(customer, field), data_put[field])

    # def test_put_fields_clean(self):
    #     client = Client()
    #     for id_customer in self.test_id_customers_clear:
    #         self._test_put_field_clean(client, id_customer, 'first_name')
    #         self._test_put_field_clean(client, id_customer, 'last_name')
    #         self._test_put_field_clean(client, id_customer, 'email', 'email_' + str(id_customer) + '_put' + '@email.com')
    #         self._test_put_field_clean(client, id_customer, 'phone')
    #         self._test_put_field_clean(client, id_customer, 'address')
    #         self._test_put_field_clean(client, id_customer, 'description')

    def test_put_first_name_clean(self):
        client = Client()
        for id_customer in self.test_id_customers_clear:
            self._test_put_field_clean(client, id_customer, 'first_name')

    def test_put_last_name_clean(self):
        client = Client()
        for id_customer in self.test_id_customers_clear:
            self._test_put_field_clean(client, id_customer, 'last_name')

    def test_put_email_clean(self):
        client = Client()
        for id_customer in self.test_id_customers_clear:
            self._test_put_field_clean(client, id_customer, 'email', 'email_' + str(id_customer) + '_put' + '@email.com')

    def test_put_phone_clean(self):
        client = Client()
        for id_customer in self.test_id_customers_clear:
            self._test_put_field_clean(client, id_customer, 'phone')

    def test_put_address_clean(self):
        client = Client()
        for id_customer in self.test_id_customers_clear:
            self._test_put_field_clean(client, id_customer, 'address')

    def test_put_description_clean(self):
        client = Client()
        for id_customer in self.test_id_customers_clear:
            self._test_put_field_clean(client, id_customer, 'description')

    # ----- DELETE -----

    # ======================================================================
    # dirty
    # ======================================================================

    # ----- GET -----

    # ----- PUT -----

    # ----- DELETE -----
