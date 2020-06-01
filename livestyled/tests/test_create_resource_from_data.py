from datetime import datetime, timedelta, timezone

from livestyled.models import Device, DeviceConsent
from livestyled.utils import create_resource_from_data


def test_create_resource_from_data():
    data = {
        '@context': '/v4/contexts/Device',
        '@id': '/v4/devices/2659',
        '@type': 'Device',
        'id': 2659,
        'token': 'EE76F4D8-BC5A-438D-9F06-9F6873F60960',
        'consent': {
            'id': 3248,
            'locationCapture': False,
            'locationGranular': None,
            'camera': False,
            'calendar': False,
            'photoSharing': False,
            'pushNotification': True,
            'createdAt': '2019-10-07T15:43:18+00:00',
            'updatedAt': '2019-10-07T15:43:18+00:00'
        },
        'type': 'IOS',
        'status': 'ACTIVE',
        'appVersion': '8.1',
        'osVersion': None,
        'model': 'iPhone 5 (GSM+CDMA)',
        'manufacturer': 'Apple',
        'bluetoothOn': None,
        'wifiConnected': None,
        'createdAt': None,
        'updatedAt': None
    }
    device = create_resource_from_data(Device, data)
    assert isinstance(device, Device)
    assert device.id == 2659
    assert isinstance(device.consent, DeviceConsent)
    assert device.consent.created_at == datetime(2019, 10, 7, 15, 43, 18, tzinfo=timezone(timedelta(0), '+0000'))
