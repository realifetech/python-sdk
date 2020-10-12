import os

from livestyled.schemas.product import ProductSchema


FIXTURES_DIR = os.path.join(os.path.dirname(__file__), 'fixtures')
TEST_API_DOMAIN = 'test.livestyled.com'


def test_deserialize_product():
    with open(os.path.join(FIXTURES_DIR, 'sell_product.json'), 'r') as fixture_file:
        product_variant = fixture_file.read()
        deserialized_product = ProductSchema().loads(product_variant)
        assert deserialized_product == {
            'status': 'active',
            'external_id': 'string',
            'translations': [
                {
                    'description': None,
                    'language': 'en',
                    'title': 'string'
                }
            ],
            'reconciliation_group': None,
            'core_product_category': None,
            'holding_time': None,
            'variants': [
                123
            ],
            'images': [
                {
                    'external_id': 'string',
                    'image_url': 'string',
                    'position': 0
                }
            ],
            'fulfilment_points': [
                123
            ],
            'id': 0,
            'modifier_lists': [
                123
            ],
            'categories': [
                123
            ],
            'reference': 'string'
        }
