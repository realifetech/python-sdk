from datetime import datetime, timedelta, timezone
import os

from livestyled.models import App, Currency, FulfilmentPoint, Order, OrderItem, Product, ProductVariant, User
from livestyled.resource_client import LiveStyledResourceClient
from livestyled.tests.utils import configure_mock_responses

FIXTURES_DIR = os.path.join(os.path.dirname(__file__), 'fixtures')
TEST_API_DOMAIN = 'test.livestyled.com'
CONTENT_TYPE = 'application/ld+json'


def test_get_orders(requests_mock):
    mock_responses = (
        ('GET', 'https://' + TEST_API_DOMAIN + '/v4/sell/orders', 'mock_responses/ls_api/orders.json', 200),
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
    assert isinstance(order_item.product, Product)
    assert order_item.product.id == 1
    assert isinstance(order_item.fulfilment_point, FulfilmentPoint)
    assert order_item.fulfilment_point.id == 1
    assert isinstance(order.user, User)
    assert order.user.id == 274814
    assert isinstance(order.app, App)
    assert isinstance(order.app.currency, Currency)
    assert order.app.currency.iso_code == 'GBP'
    assert order.app.currency.title == 'Pound'
    assert order.app.currency.sign == '£'
