from datetime import datetime, timedelta, timezone
import os

from livestyled.models.device import Device
from livestyled.models.device_preference import DevicePreference
from livestyled.models.event import Event
from livestyled.models.venue import Venue
from livestyled.resource_client import LiveStyledResourceClient
from livestyled.tests.utils import configure_mock_responses

FIXTURES_DIR = os.path.join(os.path.dirname(__file__), 'fixtures')
TEST_API_DOMAIN = 'test.livestyled.com'
CONTENT_TYPE = 'application/ld+json'


def test_get_device_preferences(requests_mock):
    mock_responses = (
        ('GET', 'https://' + TEST_API_DOMAIN + '/v4/device_preferences', 'mock_responses/ls_api/device_preferences_page1.json', 200),
        ('GET', 'https://' + TEST_API_DOMAIN + '/v4/device_preferences?page=2', 'mock_responses/ls_api/device_preferences_page2.json', 200),
    )
    configure_mock_responses(requests_mock, mock_responses, FIXTURES_DIR, CONTENT_TYPE)

    resource_client = LiveStyledResourceClient(TEST_API_DOMAIN, 'bar')
    device_preferences = list(resource_client.get_device_preferences())
    assert device_preferences
    assert len(device_preferences) == 31
    device_preference = device_preferences[0]
    assert isinstance(device_preference, DevicePreference)
    assert device_preference.venue
    assert isinstance(device_preference.venue, Venue)
    assert device_preference.venue.id == 10000918
    assert device_preference.id == 1
    assert device_preference.device
    assert isinstance(device_preference.device, Device)
    assert device_preference.device.id == 1620610
    assert not device_preference.event
    assert device_preference.created_at == datetime(2019, 2, 12, 15, 12, 46, tzinfo=timezone(timedelta(0), '+0000'))

    device_preference = device_preferences[3]
    assert isinstance(device_preference, DevicePreference)
    assert device_preference.id == 4
    assert not device_preference.venue
    assert device_preference.device
    assert isinstance(device_preference.device, Device)
    assert device_preference.device.id == 1748339
    assert device_preference.event
    assert isinstance(device_preference.event, Event)
    assert device_preference.event.id == 100015921
    assert device_preference.created_at == datetime(2019, 8, 27, 17, 19, 6, tzinfo=timezone(timedelta(0), '+0000'))


def test_get_device_preferences_default_ordering(requests_mock):
    mock_responses = (
        ('GET', 'https://' + TEST_API_DOMAIN + '/v4/device_preferences', 'mock_responses/ls_api/device_preferences_page1.json', 200),
        ('GET', 'https://' + TEST_API_DOMAIN + '/v4/device_preferences?page=2', 'mock_responses/ls_api/device_preferences_page2.json', 200),
    )
    configure_mock_responses(requests_mock, mock_responses, FIXTURES_DIR, CONTENT_TYPE)

    resource_client = LiveStyledResourceClient(TEST_API_DOMAIN, 'bar')
    list(resource_client.get_device_preferences())

    assert len(requests_mock.request_history) == 2
    assert requests_mock.request_history[0].url == 'https://test.livestyled.com/v4/device_preferences?order%5BcreatedAt%5D=desc'
