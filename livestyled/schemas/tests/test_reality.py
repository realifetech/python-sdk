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


def test_serialize_reality():
    reality = {
        'config': {},
        'created_at': datetime(2020, 9, 3, 13, 40, 6, 587000, tzinfo=timezone.utc),
        'id': 0,
        'name': 'string',
        'reality_type': 1,
        'updated_at': datetime(2020, 9, 3, 13, 40, 6, 587000, tzinfo=timezone.utc)
    }

    serialized_reality = RealitySchema().dump(reality)

    assert serialized_reality == {
        'config': {},
        'createdAt': '2020-09-03T13:40:06.587000+00:00',
        'id': 0,
        'name': 'string',
        'realityType': '/user_management/reality_types/1',
        'updatedAt': '2020-09-03T13:40:06.587000+00:00'
    }
