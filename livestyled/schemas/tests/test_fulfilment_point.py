import os

from livestyled.schemas.fulfilment_point import FulfilmentPointSchema


FIXTURES_DIR = os.path.join(os.path.dirname(__file__), 'fixtures')
TEST_API_DOMAIN = 'test.livestyled.com'


def test_deserialize_fulfilment_point():
    with open(os.path.join(FIXTURES_DIR, 'sell_fulfilment_point.json'), 'r') as fixture_file:
        fp = fixture_file.read()
        deserialized_fp = FulfilmentPointSchema().loads(fp)

        assert deserialized_fp == {
            'long': None,
            'categories': [
                3
            ],
            'type': 'VIRTUAL_QUEUE',
            'position': 1,
            'map_image_url': 'https://apiv3.s3.eu-west-1.amazonaws.com/fulfilmentpoint/02.PNG',
            'image_url': 'https://apiv3.s3.eu-west-1.amazonaws.com/fulfilmentpoint/color-wheel.png',
            'reference': "Pallavi's Bar",
            'external_id': None,
            'external_source': None,
            'status': 'ACTIVE',
            'id': 368,
            'lat': None,
            'venue': None,
            'translations': [
                {
                    'description': 'Test description: Collection point collect when ready test',
                    'title': "Pallavi's Bar",
                    'collection_note': 'Test fulfilment note: Collection point collect when ready test\r\nTest fulfilment note: Collection point collect when ready test\r\nTest fulfilment note: Collection point collect when ready test\r\nTest fulfilment note: Collection point collect when ready test\r\nTest fulfilment note: Collection point collect when ready test\r\nTest fulfilment note: Collection point collect when ready test\r\nTest fulfilment note: Collection point collect when ready test\r\nTest fulfilment note: Collection point collect when ready test\r\nTest fulfilment note: Collection point collect when ready test\r\nTest fulfilment note: Collection point collect when ready test\r\nTest fulfilment note: Collection point collect when ready test\r\nTest fulfilment note: Collection point collect when ready test',
                    'language': 'en'
                }
            ],
            'audiences': []
        }
