from django.test import TestCase
from rest_framework.test import APITestCase
from api.models import Order
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient


# Create your tests here.
class OrderTestCase(APITestCase):
    # Add your testcase here
    def setUp(self):
        print('setup')

        # self.user = User.objects.create_user(
        #     username=f'Test@TEST',
        #     password='Test'
        # )

        # self.client = APIClient()
        # self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)

        self.client.login(username='Test@TEST', password='Test')

        self.test_url = '/api/import-order/'
    
    def test_list_order(self):

        # 'Content-type': 'application/json',
        mheaders = {
            'content_type': 'application/json',
            'HTTP_X_mykey': 'omni_pretest_token'
        }

        print(
            'testlist'
        )

        Order.objects.create(
            order_num ='A00013',
            total_price = 99.99
        )
        # self.client.headers.update({'Mykey': 'omni_pretest_token'})
        r = self.client.get(self.test_url, **mheaders)

        result = r.json()
        print('--------Here is the result', result)

        # self.assertEqual(len(result), 1)
        self.assertEqual(result[0].name, 'A00013')
        self.assertEqual(result[0].price, 99.99)
    
    # pass

# class SomeThingTest(APITestCase):

#     def setUp(self):
#         print('setup')
#         self.user = User.objects.create_user(
#            username=f'Test@TEST',
#            password='Test'
#         )

#         self.client.login(username='Test@TEST', password='Test')

#         self.test_url = '/api/food/'
    
#     def test_list_food(self):

#         print(
#             'testlist'
#         )
#         Food.objects.create(
#             name='food1',
#             price=123456
#         )

#         r = self.client.get(self.test_url)

#         result = r.json()

#         self.assertEqual(len(result), 1)
#         self.assertEqual(result[0].name, 'food1')
#         self.assertEqual(result[0].price, 123456)