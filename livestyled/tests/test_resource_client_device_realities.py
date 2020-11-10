import json
import os

from livestyled.models import Device, DeviceReality, Reality
from livestyled.resource_client import LiveStyledResourceClient
from livestyled.tests.utils import configure_mock_responses

FIXTURES_DIR = os.path.join(os.path.dirname(__file__), 'fixtures')
TEST_API_DOMAIN = 'test.livestyled.com'
CONTENT_TYPE = 'application/ld+json'


def test_create_device_reality(requests_mock):
    mock_responses = (
        ('POST', 'https://' + TEST_API_DOMAIN + '/v4/user_management/device_realities', 'mock_responses/ls_api/user_management/new_device_reality.json', 200),
    )
    configure_mock_responses(requests_mock, mock_responses, FIXTURES_DIR, CONTENT_TYPE)

    resource_client = LiveStyledResourceClient(TEST_API_DOMAIN, 'bar')
    device_reality = DeviceReality.create_new(
        device=Device.placeholder(id=1),
        reality=Reality.placeholder(id=9),
        value='is this the real reality'
    )
    resource_client.create_device_reality(device_reality)

    assert len(requests_mock.request_history) == 1
    assert requests_mock.request_history[0].method == 'POST'
    assert requests_mock.request_history[0].url == 'https://test.livestyled.com/v4/user_management/device_realities'
    assert json.loads(requests_mock.request_history[0].body) == {
        'value': 'is this the real reality',
        'device': '/user_management/devices/1',
        'reality': '/user_management/realities/9'
    }
