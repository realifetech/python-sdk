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
                    'product': {
                        'categories': [
                            {
                                'id': 1,
                                'position': 1,
                                'reference': 'Kartiks product Category'
                            }
                        ],
                        'id': 1,
                        'images': [],
                        'reference': 'Plant',
                        'status': 'ACTIVE',
                        'translations': [],
                        'variants': [],
                        'fulfilment_points': [],
                        'external_id': None,
                        'holding_time': None,
                        'modifier_lists': [],
                        'reconciliation_group': None,
                        'core_product_category': None,
                    },
                    'fulfilment_point': {
                        'categories': [
                            {
                                'id': 1,
                                'status': 'ACTIVE',
                                'translations': [
                                    {
                                        'id': 1,
                                        'language': 'en',
                                        'title': 'Kartiks '
                                                 'Collection '
                                                 'Point '
                                                 'Category'}
                                ]
                            }
                        ],
                        'id': 1,
                        'image_url': 'https://apiv3.s3.eu-west-1.amazonaws.com/fulfilmentpoint/German-Shepherd-Puppy-Fetch.jpg',
                        'lat': '38.026641',
                        'long': '38.026641',
                        'map_image_url': 'https://apiv3.s3.eu-west-1.amazonaws.com/fulfilmentpoint/british_summer_time_map_bigger.jpg',
                        'position': 0,
                        'status': 'ACTIVE',
                        'reference': 'kartiks Collection point',
                        'translations': [
                            {
                                'collection_note': 'Fulfillment '
                                                   'note',
                                'description': 'Description',
                                'id': 1,
                                'language': 'en',
                                'title': 'Fulfilment point '
                                         '1'
                            }
                        ],
                        'type': 'COLLECTION',
                        'venue': 10000974
                    },
                    'id': 1,
                    'image_url': 'https://apiv3.s3.eu-west-1.amazonaws.com/productimage/Web-Homepage-graphic-1.jpg',
                    'price': 1,
                    'product_variant': {
                        'id': 1,
                        'price': 0,
                        'stocks': [
                            '/v4/product_variant_stocks/fulfilmentPoint=1;productVariant=1'
                        ]
                    },
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
            'updated_at': datetime(2020, 5, 27, 8, 48, 14, tzinfo=timezone(timedelta(0), '+0000')),
            'user': {
                'auth_type': None,
                'email': 'test@gmail.com',
                'id': 274814,
                'token': 'd290fab6-9f89-413d-a89b-9dd5dbcd8eb4',
                'user_info': {
                    'dob': datetime(2020, 4, 30, 0, 0, tzinfo=timezone(timedelta(0), '+0000')),
                    'first_name': 'string',
                    'gender': 'MALE',
                    'last_name': 'string',
                    'phone': '+4712345678'
                }
            }
        }
