from datetime import datetime, timedelta, timezone
import os

from livestyled.models import FulfilmentPoint, FulfilmentPointCategory, FulfilmentPointCategoryTranslation, FulfilmentPointTranslation, Order, OrderItem, Product, ProductCategory, ProductVariant, User
from livestyled.resource_client import LiveStyledResourceClient
from livestyled.tests.utils import configure_mock_responses

FIXTURES_DIR = os.path.join(os.path.dirname(__file__), 'fixtures')
TEST_API_DOMAIN = 'test.livestyled.com'
CONTENT_TYPE = 'application/ld+json'


def test_get_orders(requests_mock):
    mock_responses = (
        ('GET', 'https://' + TEST_API_DOMAIN + '/v4/orders', 'mock_responses/ls_api/orders.json', 200),
    )
    configure_mock_responses(requests_mock, mock_responses, FIXTURES_DIR, CONTENT_TYPE)

    resource_client = LiveStyledResourceClient(TEST_API_DOMAIN, 'bar')
    orders = list(resource_client.get_orders())
    assert len(orders) == 30
    orders.sort(key=lambda o: o.id)
    order = orders[0]
    assert isinstance(order, Order)
    assert order.id == 1
    assert order.status == 'COMPLETE'
    assert order.gross_amount == 1
    assert order.discount == 0
    assert order.net_amount == 1
    assert order.order_number == 12345678
    assert order.created_at == datetime(2019, 7, 4, 7, 43, 53, tzinfo=timezone(timedelta(0), '+0000'))
    assert order.updated_at == datetime(2020, 5, 27, 8, 48, 14, tzinfo=timezone(timedelta(0), '+0000'))
    assert len(order.items) == 1
    assert isinstance(order.items[0], OrderItem)
    order_item = order.items[0]
    assert order_item.id == 1
    assert order_item.quantity == 1
    assert order_item.title == 'Kartiks 1st Product'
    assert order_item.subtitle == 'TEST Product'
    assert order_item.image_url == 'https://apiv3.s3.eu-west-1.amazonaws.com/productimage/Web-Homepage-graphic-1.jpg'
    assert order_item.price == 1
    assert order_item.total_price == 1
    assert isinstance(order_item.product_variant, ProductVariant)
    assert order_item.product_variant.id == 1
    assert order_item.product_variant.price == 0
    assert order_item.product_variant.stocks == [
        '/v4/product_variant_stocks/fulfilmentPoint=1;productVariant=1'
    ]
    assert isinstance(order_item.product, Product)
    assert order_item.product.id == 1
    assert order_item.product.status == 'ACTIVE'
    assert order_item.product.reference == 'Plant'
    assert order_item.product.images == []
    assert len(order_item.product.categories) == 1
    assert isinstance(order_item.product.categories[0], ProductCategory)
    assert order_item.product.categories[0].id == 1
    assert order_item.product.categories[0].reference == 'Kartiks product Category'
    assert order_item.product.categories[0].position == 1
    assert isinstance(order_item.fulfilment_point, FulfilmentPoint)
    assert order_item.fulfilment_point.id == 1
    assert order_item.fulfilment_point.status == 'ACTIVE'
    assert order_item.fulfilment_point.reference == 'kartiks Collection point'
    assert order_item.fulfilment_point.image_url == 'https://apiv3.s3.eu-west-1.amazonaws.com/fulfilmentpoint/German-Shepherd-Puppy-Fetch.jpg'
    assert order_item.fulfilment_point.map_image_url == 'https://apiv3.s3.eu-west-1.amazonaws.com/fulfilmentpoint/british_summer_time_map_bigger.jpg'
    assert order_item.fulfilment_point.lat == '38.026641'
    assert order_item.fulfilment_point.long == '38.026641'
    assert order_item.fulfilment_point.type == 'COLLECTION'
    assert order_item.fulfilment_point.position == 0
    assert len(order_item.fulfilment_point.translations) == 1
    assert isinstance(order_item.fulfilment_point.translations[0], FulfilmentPointTranslation)
    assert order_item.fulfilment_point.translations[0].id == 1
    assert order_item.fulfilment_point.translations[0].language == 'en'
    assert order_item.fulfilment_point.translations[0].description == 'Description'
    assert order_item.fulfilment_point.translations[0].title == 'Fulfilment point 1'
    assert order_item.fulfilment_point.translations[0].collection_note == 'Fulfillment note'
    assert len(order_item.fulfilment_point.categories) == 1
    assert isinstance(order_item.fulfilment_point.categories[0], FulfilmentPointCategory)
    assert order_item.fulfilment_point.categories[0].id == 1
    assert order_item.fulfilment_point.categories[0].status == 'ACTIVE'
    assert len(order_item.fulfilment_point.categories[0].translations) == 1
    assert isinstance(order_item.fulfilment_point.categories[0].translations[0], FulfilmentPointCategoryTranslation)
    assert order_item.fulfilment_point.categories[0].translations[0].id == 1
    assert order_item.fulfilment_point.categories[0].translations[0].language == 'en'
    assert order_item.fulfilment_point.categories[0].translations[0].title == 'Kartiks Collection Point Category'
    assert isinstance(order.user, User)
    assert order.user.id == 274814
    assert order.user.email == 'test@gmail.com'
    assert order.user.token == 'd290fab6-9f89-413d-a89b-9dd5dbcd8eb4'
    assert order.user.user_info.first_name == 'string'
    assert order.user.user_info.last_name == 'string'
    assert order.user.user_info.gender == 'MALE'
    assert order.user.user_info.phone == '+4712345678'
    assert order.user.user_info.dob == datetime(2020, 4, 30, 0, 0, tzinfo=timezone(timedelta(0), '+0000'))
