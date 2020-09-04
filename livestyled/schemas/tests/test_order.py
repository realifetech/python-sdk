from datetime import datetime, timedelta, timezone
import os

from livestyled.schemas.order import OrderSchema


FIXTURES_DIR = os.path.join(os.path.dirname(__file__), 'fixtures')
TEST_API_DOMAIN = 'test.livestyled.com'
CONTENT_TYPE = 'application/ld+json'


def test_deserialize_order():
    with open(os.path.join(FIXTURES_DIR, 'order.json'), 'r') as fixture_file:
        order = fixture_file.read()
        deserialized_order = OrderSchema().loads(order)

        assert deserialized_order == {
            'created_at': datetime(2019, 7, 4, 7, 43, 53, tzinfo=timezone(timedelta(0), '+0000')),
            'discount': 0,
            'gross_amount': 1,
            'id': 1,
            'app': {
                'api_keys': None,
                'code': None,
                'cohorts': None,
                'currency': {
                    'id': None,
                    'iso_code': 'GBP',
                    'sign': '£',
                    'title': 'Pound'
                },
                'deeplink_namespace': None,
                'email': None,
                'google_api_key': None,
                'id': None,
                'merchant_accounts': None,
                'name': None,
                'password': None,
                'payment_gateway': None,
                'roles': None,
                'salt': None,
                'sender_email': None,
                'status': None,
                'timezone': None,
                'title': None,
                'token': None,
                'username': None,
                'venues': None
            },
            'items': [
                {
                    'product': 1,
                    'fulfilment_point': 1,
                    'id': 1,
                    'image_url': 'https://apiv3.s3.eu-west-1.amazonaws.com/productimage/Web-Homepage-graphic-1.jpg',
                    'price': 1,
                    'product_variant': 1,
                    'quantity': 1,
                    'subtitle': 'TEST Product',
                    'title': 'Kartiks 1st Product',
                    'total_price': 1
                }
            ],
            'net_amount': 1,
            'order_amount': None,
            'order_number': 12345678,
            'status': 'COMPLETE',
            'estimated_at': None,
            'collection_date': None,
            'updated_at': datetime(2020, 5, 27, 8, 48, 14, tzinfo=timezone(timedelta(0), '+0000')),
            'user': 274814,
            'fulfilment_point': None
        }
