from datetime import datetime
import os

from livestyled.models.audience_device import AudienceDevice
from livestyled.resource_client import LiveStyledResourceClient
from livestyled.tests.utils import configure_mock_responses

FIXTURES_DIR = os.path.join(os.path.dirname(__file__), 'fixtures')
TEST_API_DOMAIN = 'test.livestyled.com'
CONTENT_TYPE = 'application/ld+json'


def test_audience_creation_duplicate(requests_mock):
    mock_responses = (
        ('POST', 'https://' + TEST_API_DOMAIN + '/v4/user_management/audience_devices',
         'mock_responses/ls_api/user_management/create_audience_500_response.json', 500),
    )
    configure_mock_responses(requests_mock, mock_responses, FIXTURES_DIR, CONTENT_TYPE)

    resource_client = LiveStyledResourceClient(TEST_API_DOMAIN, 'bar')
    audience_device = AudienceDevice({
        'id': 1, 'name': 'name', 'reality_values': [], 'updated_at': datetime.now(), 'created_at': datetime.now()
    }, {
        'id': 1,
        'token': 'name',
        'consent': {},
        'push_consents': [],
        'status': 'active',
        'type': 'active',
        'app_version': 'active',
        'os_version': 'active',
        'model': 'active',
        'manufacturer': 'active',
        'bluetooth_on': 'active',
        'wifi_connected': 'active',
        'updated_at': datetime.now(),
        'created_at': datetime.now()
    })

    res = resource_client.create_audience_device(audience_device=audience_device)

    assert audience_device == res


def test_audience_creation_duplicate_adverse_response(requests_mock):
    mock_responses = (
        ('POST', 'https://' + TEST_API_DOMAIN + '/v4/user_management/audience_devices',
         'mock_responses/ls_api/user_management/create_audience_500_response_2.json', 500),
    )
    configure_mock_responses(requests_mock, mock_responses, FIXTURES_DIR, CONTENT_TYPE)

    resource_client = LiveStyledResourceClient(TEST_API_DOMAIN, 'bar')
    audience_device = AudienceDevice({
        'id': 1, 'name': 'name', 'reality_values': [], 'updated_at': datetime.now(), 'created_at': datetime.now()
    }, {
        'id': 1,
        'token': 'name',
        'consent': {},
        'push_consents': [],
        'status': 'active',
        'type': 'active',
        'app_version': 'active',
        'os_version': 'active',
        'model': 'active',
        'manufacturer': 'active',
        'bluetooth_on': 'active',
        'wifi_connected': 'active',
        'updated_at': datetime.now(),
        'created_at': datetime.now()
    })

    res = resource_client.create_audience_device(audience_device=audience_device)

    assert audience_device == res
