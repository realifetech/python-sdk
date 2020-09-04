from datetime import datetime, timedelta, timezone
import os

from livestyled.models import Product, ProductImage, ProductTranslation
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
    assert isinstance(product.images[0], ProductImage)
    assert product.images[0].id == 4
    assert product.images[0].position == 1
    assert product.images[0].created_at is None
    assert product.images[0].updated_at is None
    assert product.images[0].external_id == "6N6H3B3IZVGBK3OMFOCFNGE2"
    assert product.images[0].image_url == 'https://apiv3.s3.eu-west-1.amazonaws.com/productimage/original-2.jpeg'
    assert product.images[0].product.id == 3
    assert len(product.translations) == 1
    assert isinstance(product.translations[0], ProductTranslation)
    assert product.translations[0].id == 101138
    assert product.translations[0].title == "Men's Tank"
    assert product.translations[0].description is None
    assert product.translations[0].language == 'en'
    assert product.translations[0].created_at is None
    assert product.translations[0].updated_at is None
