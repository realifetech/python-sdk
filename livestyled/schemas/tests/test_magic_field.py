import os

from livestyled.schemas.magic_field import MagicFieldSchema


FIXTURES_DIR = os.path.join(os.path.dirname(__file__), 'fixtures')
TEST_API_DOMAIN = 'test.livestyled.com'


def test_deserialize_league_table():
    with open(os.path.join(FIXTURES_DIR, 'magic_field.json'), 'r') as fixture_file:
        magic_field = fixture_file.read()
        deserialized_magic_field = MagicFieldSchema().loads(magic_field)
        assert deserialized_magic_field == {
            'id': 1,
            'key': 'wristbandId',
            'value': 'ABCDEF',
            'user_id': 274814
        }
