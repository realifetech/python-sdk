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
        ('GET', 'https://' + TEST_API_DOMAIN + '/v4/products', 'mock_responses/ls_api/products.json', 200),
    )
    configure_mock_responses(requests_mock, mock_responses, FIXTURES_DIR, CONTENT_TYPE)

    resource_client = LiveStyledResourceClient(TEST_API_DOMAIN, 'bar')
    products = list(resource_client.get_products())
    assert len(products) == 30
    products.sort(key=lambda o: o.id)
    product = products[1]

    assert isinstance(product, Product)
    assert product.id == 2
    assert product.status == 'ACTIVE'
    assert product.reference == "Amy's product"
    assert len(product.images) == 1
    assert isinstance(product.images[0], ProductImage)
    assert product.images[0].id == 3
    assert product.images[0].position == 1
    assert product.images[0].created_at == datetime(2019, 7, 23, 11, 9, 57, tzinfo=timezone(timedelta(0), '+0000'))
    assert product.images[0].updated_at == datetime(2019, 11, 8, 11, 19, 31, tzinfo=timezone(timedelta(0), '+0000'))
    assert product.images[0].external_id is None
    assert product.images[0].image_url == 'https://apiv3.s3.eu-west-1.amazonaws.com/productimage/corgi%20bum.png'
    assert product.images[0].product.id == 2
    assert len(product.translations) == 1
    assert isinstance(product.translations[0], ProductTranslation)
    assert product.translations[0].id == 2
    assert product.translations[0].title == "Amy's product"
    assert product.translations[0].description == "A vegan burger from Beyond Meat with vegan smoked Gouda, Rubies in the Rubble Chipotle ‘Mayo’, mustard, red onion, pickles and lettuce.\r\n\r\nAfter a successful trial at our King's Cross restaurant, we're finally rolling out the Plant burger to every single Honest Burgers restaurant!\r\n\r\nThe Beyond Meat patty that goes into this burger is the result of over seven years of product development to look, cook and taste like beef. It also packs 20 grams of plant-based protein and has no GMOs, soy or gluten.\r\n\r\nA vegan burger from Beyond Meat with vegan smoked Gouda, Rubies in the Rubble Chipotle ‘Mayo’, mustard, red onion, pickles and lettuce.\r\n\r\nAfter a successful trial at our King's Cross restaurant, we're finally rolling out the Plant burger to every single Honest Burgers restaurant!\r\n\r\nThe Beyond Meat patty that goes into this burger is the result of over seven years of product development to look, cook and taste like beef. It also packs 20 grams of plant-based protein and has no GMOs, soy or gluten.\r\n\r\nA vegan burger from Beyond Meat with vegan smoked Gouda, Rubies in the Rubble Chipotle ‘Mayo’, mustard, red onion, pickles and lettuce.\r\n\r\nAfter a successful trial at our King's Cross restaurant, we're finally rolling out the Plant burger to every single Honest Burgers restaurant!\r\n\r\nThe Beyond Meat patty that goes into this burger is the result of over seven years of product development to look, cook and taste like beef. It also packs 20 grams of plant-based protein and has no GMOs, soy or gluten."
    assert product.translations[0].language == 'en'
    assert product.translations[0].created_at == datetime(2019, 7, 23, 11, 0, 2, tzinfo=timezone(timedelta(0), '+0000'))
    assert product.translations[0].updated_at == datetime(2019, 7, 25, 11, 30, 36, tzinfo=timezone(timedelta(0), '+0000'))
