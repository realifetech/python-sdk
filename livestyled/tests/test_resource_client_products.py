import json
import os

from livestyled.models import Product
from livestyled.resource_client import LiveStyledResourceClient
from livestyled.tests.utils import configure_mock_responses

FIXTURES_DIR = os.path.join(os.path.dirname(__file__), 'fixtures')
TEST_API_DOMAIN = 'test.livestyled.com'
CONTENT_TYPE = 'application/ld+json'


def test_get_products(requests_mock):
    mock_responses = (
        ('GET', 'https://' + TEST_API_DOMAIN + '/v4/sell/products', 'mock_responses/ls_api/products.json', 200),
    )
    configure_mock_responses(requests_mock, mock_responses, FIXTURES_DIR, CONTENT_TYPE)

    resource_client = LiveStyledResourceClient(TEST_API_DOMAIN, 'bar')
    products = list(resource_client.get_products())
    assert len(products) == 30
    products.sort(key=lambda o: o.id)
    product = products[2]

    assert isinstance(product, Product)
    assert product.id == 3
    assert product.status == 'ACTIVE'
    assert product.reference == "Men's Tank"
    assert len(product.images) == 1
    assert isinstance(product.images[0], dict)
    assert product.images[0] == {
        'external_id': '6N6H3B3IZVGBK3OMFOCFNGE2',
        'image_url': 'https://apiv3.s3.eu-west-1.amazonaws.com/productimage/original-2.jpeg',
        'position': 1
    }
    assert len(product.translations) == 1
    assert product.translations[0]['title'] == "Men's Tank"
    assert product.translations[0]['description'] is None
    assert product.translations[0]['language'] == 'en'


def test_create_product(requests_mock):
    resource_client = LiveStyledResourceClient(TEST_API_DOMAIN, 'bar')
    mock_responses = (
        ('POST', 'https://' + TEST_API_DOMAIN + '/v4/sell/products', 'mock_responses/ls_api/sell/new_product.json', 200),
    )
    configure_mock_responses(requests_mock, mock_responses, FIXTURES_DIR, CONTENT_TYPE)

    resource_client.create_product(
        Product.create_new(
            external_id='testproduct1',
            categories=None,
            status='ACTIVE',
            reference='Test Product 1',
            translations=[
                {
                    'language': 'en',
                    'title': 'Test Product 1',
                    'description': 'This is a Test Product'
                }
            ],
            price=100,
            fulfilment_points=[],
            core_product_category=None,
            holding_time=None,
            images=None,
            modifier_lists=None,
            reconciliation_group=None,
            variants=None,
        )
    )

    assert len(requests_mock.request_history) == 1
    assert requests_mock.request_history[0].method == 'POST'
    assert requests_mock.request_history[0].url == 'https://' + TEST_API_DOMAIN + '/v4/sell/products'
    assert json.loads(requests_mock.request_history[0].body) == {
        'externalId': 'testproduct1',
        'reference': 'Test Product 1',
        'status': 'ACTIVE',
        'translations': [
            {
                'description': 'This is a Test Product',
                'language': 'en',
                'title': 'Test Product 1'
            }
        ],
        'images': [],
        'categories': [],
        'fulfilmentPoints': [],
        'modifierLists': [],
        'variants': []
    }
