from django.test import TestCase
from customers.models import Customer
import datetime


# Create your tests here.
class CustomerTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        pass

    def setUp(self):
        # self.date_today = datetime.datetime.today()
        # print('self.date_today', self.date_today)
        # self.timedelta = datetime.timedelta(days=1)
        # print('self.timedelta', self.timedelta)
        # self.date_create = self.date_today + self.timedelta
        # print('self.date_create', self.date_create)
        self.date_today = datetime.datetime.now(datetime.timezone.utc)

        self.customer = Customer.objects.create(
            first_name='first_name_000',
            last_name='last_name_000',
        )
        self.customer.save()

    def tearDown(self):
        self.customer.delete()

    # ======================================================================

    # ----- fields options -----

    def _test_field_verbose_name(self, field, verbose_name_expected):
        customer = Customer.objects.get(id=1)
        verbose_name = customer._meta.get_field(field).verbose_name
        self.assertEquals(verbose_name, verbose_name_expected)

    def _test_field_max_length(self, field, max_length_expected):
        customer = Customer.objects.get(id=1)
        max_length = customer._meta.get_field(field).max_length
        self.assertEquals(max_length, max_length_expected)

    # first_name
    def test_first_name_verbose_name(self):
        self._test_field_verbose_name('first_name', 'First name')

    def test_first_name_max_length(self):
        self._test_field_max_length('first_name', 255)

    # last_name
    def test_last_name_verbose_name(self):
        self._test_field_verbose_name('last_name', 'Last name')

    def test_last_name_max_length(self):
        self._test_field_max_length('last_name', 255)

    # email

    # phone
    def test_phone_max_length(self):
        self._test_field_max_length('phone', 20)

    # address
    def test_address_null(self):
        customer = Customer.objects.get(id=1)
        address = customer.address
        self.assertEquals(address, None)

    # description
    def test_description_null(self):
        customer = Customer.objects.get(id=1)
        description = customer.description
        self.assertEquals(description, None)

    # date_create
    def test_date_create_verbose_name(self):
        self._test_field_verbose_name('date_create', 'Date created')

    def test_date_create_auto_now_add(self):
        customer = Customer.objects.get(id=1)
        date_create = customer.date_create
        date_max_limit = self.date_today + datetime.timedelta(milliseconds=1)
        self.assertGreaterEqual(date_create, self.date_today)
        self.assertLess(date_create, date_max_limit)

    # ----- fields update -----

    def _test_update_field(self, field, field_value_new=None):
        customer = Customer.objects.get(id=1)
        if not field_value_new:
            field_value = getattr(customer, field)
            field_value_new = field_value + '_new'
        setattr(customer, field, field_value_new)
        customer.save()
        customer = Customer.objects.get(id=1)
        field_value = getattr(customer, field)
        self.assertEquals(field_value, field_value_new)

    # first_name
    def test_update_first_name(self):
        self._test_update_field('first_name')

    # last_name
    def test_update_last_name(self):
        self._test_update_field('last_name')

    # email
    def test_update_email(self):
        # TODO Why can I set such email? Where is validations?
        self._test_update_field('email', 'email_000')

    # phone
    def test_update_phone(self):
        self._test_update_field('phone', 'phone_000')

    # address
    def test_update_address(self):
        self._test_update_field('address', 'address_000')

    # description
    def test_update_description(self):
        self._test_update_field('description', 'description_000')

    # date_create
    def test_update_date_create_auto_now_add(self):
        customer = Customer.objects.get(id=1)
        date_create = customer.date_create
        date_create_new = date_create + datetime.timedelta(days=1)
        self.assertEquals(type(date_create), type(date_create_new))
        self.assertNotEquals(date_create, date_create_new)

    # ----- functions -----

    def test_object_str(self):
        customer = Customer.objects.get(id=1)
        expected_object_name = '%s %s' % (customer.first_name, customer.last_name)
        self.assertEquals(expected_object_name, str(customer))

    # ======================================================================
