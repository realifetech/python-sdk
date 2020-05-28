import os

from livestyled.models.device import Device
from livestyled.resource_client import LiveStyledResourceClient
from livestyled.tests.utils import configure_mock_responses

FIXTURES_DIR = os.path.join(os.path.dirname(__file__), 'fixtures')
TEST_API_DOMAIN = 'test.livestyled.com'
CONTENT_TYPE = 'application/ld+json'


def test_get_device_by_id(requests_mock):
    mock_responses = (
        ('GET', 'https://' + TEST_API_DOMAIN + '/v4/devices/1234', 'mock_responses/ls_api/device_1234.json', 200),
    )
    configure_mock_responses(requests_mock, mock_responses, FIXTURES_DIR, CONTENT_TYPE)

    resource_client = LiveStyledResourceClient(TEST_API_DOMAIN, 'bar')
    device = resource_client.get_device(1234)
    assert device
    assert isinstance(device, Device)
    assert device.id == 1234
    assert device.push_consents == []
