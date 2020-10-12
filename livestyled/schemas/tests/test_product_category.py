import os

from livestyled.schemas.product import ProductCategorySchema


FIXTURES_DIR = os.path.join(os.path.dirname(__file__), 'fixtures')
TEST_API_DOMAIN = 'test.livestyled.com'


def test_deserialize_product_category():
    with open(os.path.join(FIXTURES_DIR, 'sell_product_category.json'), 'r') as fixture_file:
        product_variant = fixture_file.read()
        deserialized_product_category = ProductCategorySchema().loads(product_variant)
        assert deserialized_product_category == {
            'translations': [
                {
                    'title': 'string',
                    'language': 'en'
                }
            ],
            'position': 0,
            'status': 'string',
            'id': 0,
            'external_id': 'string',
            'reference': 'string'
        }
