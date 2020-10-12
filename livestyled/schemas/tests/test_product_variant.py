import os

from livestyled.schemas.product import ProductVariantSchema


FIXTURES_DIR = os.path.join(os.path.dirname(__file__), 'fixtures')
TEST_API_DOMAIN = 'test.livestyled.com'


def test_deserialize_product_variant():
    with open(os.path.join(FIXTURES_DIR, 'sell_product_variant.json'), 'r') as fixture_file:
        product_variant = fixture_file.read()
        deserialized_product_variant = ProductVariantSchema().loads(product_variant)
        assert deserialized_product_variant == {
            'stocks': [
                123
            ],
            'price': 0,
            'id': 0,
            'product': 123,
            'external_id': 'string',
            'translations': [
                {
                    'language': 'en',
                    'title': 'string'
                }
            ]
        }
