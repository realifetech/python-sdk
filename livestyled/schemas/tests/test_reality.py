from datetime import datetime, timezone
import os

from livestyled.schemas.reality import RealitySchema


FIXTURES_DIR = os.path.join(os.path.dirname(__file__), 'fixtures')
TEST_API_DOMAIN = 'test.livestyled.com'


def test_deserialize_reality():
    with open(os.path.join(FIXTURES_DIR, 'user_management/reality.json'), 'r') as fixture_file:
        reality = fixture_file.read()
        deserialized_reality = RealitySchema().loads(reality)
        assert deserialized_reality == {
            'config': {},
            'created_at': datetime(2020, 9, 3, 13, 40, 6, 587000, tzinfo=timezone.utc),
            'id': 0,
            'name': 'string',
            'reality_type': 1,
            'updated_at': datetime(2020, 9, 3, 13, 40, 6, 587000, tzinfo=timezone.utc)
        }
