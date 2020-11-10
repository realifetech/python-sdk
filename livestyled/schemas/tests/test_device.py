from datetime import datetime, timedelta, timezone
import os

from livestyled.schemas.device import DeviceSchema


FIXTURES_DIR = os.path.join(os.path.dirname(__file__), 'fixtures')
TEST_API_DOMAIN = 'test.livestyled.com'


def test_deserialize_device():
    with open(os.path.join(FIXTURES_DIR, 'example_device.json'), 'r') as fixture_file:
        device = fixture_file.read()
        deserialized_device = DeviceSchema().loads(device)
        assert deserialized_device == {
            'id': 1754392,
            'token': 'A12B149B-20C1-4958-B85F-4D248123456',
            'push_consents': [],
            'type': 'IOS',
            'status': 'ACTIVE',
            'app_version': '10.8',
            'os_version': '13.3',
            'model': 'Simulator',
            'manufacturer': 'APPLE',
            'bluetooth_on': False,
            'wifi_connected': True,
            'created_at': datetime(2020, 2, 5, 14, 29, 40, tzinfo=timezone(timedelta(0), '+0000')),
            'updated_at': datetime(2020, 2, 5, 14, 29, 40, tzinfo=timezone(timedelta(0), '+0000')),
            'consent': {
                'calendar': False,
                'camera': False,
                'id': 4299,
                'location_capture': True,
                'location_granular': 'appInUse',
                'photo_sharing': False,
                'push_notification': True,
                'created_at': datetime(2020, 2, 5, 14, 29, 53, tzinfo=timezone(timedelta(0), '+0000')),
                'updated_at': datetime(2020, 2, 5, 14, 29, 56, tzinfo=timezone(timedelta(0), '+0000'))
            }
        }


def test_deserialize_device_no_push_consents():
    with open(os.path.join(FIXTURES_DIR, 'example_device_no_push_consents.json'), 'r') as fixture_file:
        device = fixture_file.read()
        deserialized_device = DeviceSchema().loads(device)
        assert deserialized_device == {
            'id': 1754392,
            'token': 'A12B149B-20C1-4958-B85F-4D248123456',
            'push_consents': None,
            'type': 'IOS',
            'status': 'ACTIVE',
            'app_version': '10.8',
            'os_version': '13.3',
            'model': 'Simulator',
            'manufacturer': 'APPLE',
            'bluetooth_on': False,
            'wifi_connected': True,
            'created_at': datetime(2020, 2, 5, 14, 29, 40, tzinfo=timezone(timedelta(0), '+0000')),
            'updated_at': datetime(2020, 2, 5, 14, 29, 40, tzinfo=timezone(timedelta(0), '+0000')),
            'consent': {
                'calendar': False,
                'camera': False,
                'id': 4299,
                'location_capture': True,
                'location_granular': 'appInUse',
                'photo_sharing': False,
                'push_notification': True,
                'created_at': datetime(2020, 2, 5, 14, 29, 53, tzinfo=timezone(timedelta(0), '+0000')),
                'updated_at': datetime(2020, 2, 5, 14, 29, 56, tzinfo=timezone(timedelta(0), '+0000'))
            }
        }
