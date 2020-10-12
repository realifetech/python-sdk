from datetime import datetime, timezone
import os

from livestyled.schemas.device_reality import DeviceRealitySchema


FIXTURES_DIR = os.path.join(os.path.dirname(__file__), 'fixtures')
TEST_API_DOMAIN = 'test.livestyled.com'


def test_deserialize_device_reality():
    with open(os.path.join(FIXTURES_DIR, 'user_management/device_reality.json'), 'r') as fixture_file:
        device_reality = fixture_file.read()
        deserialized_device_reality = DeviceRealitySchema().loads(device_reality)
        assert deserialized_device_reality == {
            'created_at': datetime(2020, 9, 3, 12, 9, 45, 932000, tzinfo=timezone.utc),
            'device': 9,
            'reality': 1,
            'updated_at': datetime(2020, 9, 3, 12, 9, 45, 932000, tzinfo=timezone.utc),
            'value': 'true'
        }
