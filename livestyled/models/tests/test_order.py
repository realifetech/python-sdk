import json
import os

from livestyled.models.order import Order
from livestyled.utils import create_resource_from_data

FIXTURES_DIR = os.path.join(os.path.dirname(__file__), 'fixtures')


def test_create_order_model():
    with open(os.path.join(FIXTURES_DIR, 'order.json'), 'r') as fixture_file:
        order_data = json.loads(fixture_file.read())

    order = create_resource_from_data(Order, order_data)

    assert isinstance(order, Order)
