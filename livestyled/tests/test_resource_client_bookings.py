from datetime import datetime, timedelta, timezone
import json
import os

import pytest

from livestyled.models.booking import Booking
from livestyled.models.device import Device
from livestyled.models.event import Event
from livestyled.models.user import User
from livestyled.resource_client import LiveStyledResourceClient
from livestyled.tests.utils import configure_mock_responses

FIXTURES_DIR = os.path.join(os.path.dirname(__file__), 'fixtures')
TEST_API_DOMAIN = 'test.livestyled.com'
CONTENT_TYPE = 'application/ld+json'


def test_get_bookings(requests_mock):
    mock_responses = (
        ('GET', 'https://' + TEST_API_DOMAIN + '/v4/bookings', 'mock_responses/ls_api/bookings_page1.json', 200),
        ('GET', 'https://' + TEST_API_DOMAIN + '/v4/bookings?page=2', 'mock_responses/ls_api/bookings_page2.json', 200),
    )
    configure_mock_responses(requests_mock, mock_responses, FIXTURES_DIR, CONTENT_TYPE)

    resource_client = LiveStyledResourceClient(TEST_API_DOMAIN, 'bar')
    bookings = list(resource_client.get_bookings())
    assert bookings
    assert len(bookings) == 60
    booking = bookings[0]
    assert isinstance(booking, Booking)
    assert booking.type == 'e-ticket'
    assert booking.id == 16
    assert booking.device
    assert isinstance(booking.device, Device)
    assert booking.device.id == 1748495
    assert booking.user
    assert isinstance(booking.user, User)
    assert booking.user.id == 276270
    assert booking.event
    assert isinstance(booking.event, Event)
    assert booking.event.id == 100015938
    assert booking.created_at == datetime(2019, 8, 16, 9, 58, 35, tzinfo=timezone(timedelta(0), '+0000'))
    assert booking.updated_at == datetime(2019, 8, 16, 9, 58, 35, tzinfo=timezone(timedelta(0), '+0000'))
    assert booking.action == 'going'

    booking = bookings[3]
    assert isinstance(booking, Booking)
    assert booking.type == 'manual'
    assert booking.id == 53
    assert booking.device
    assert isinstance(booking.device, Device)
    assert booking.device.id == 1748495
    assert not booking.user
    assert booking.event
    assert isinstance(booking.event, Event)
    assert booking.event.id == 100015860
    assert booking.created_at == datetime(2019, 8, 21, 13, 31, 47, tzinfo=timezone(timedelta(0), '+0000'))
    assert booking.updated_at == datetime(2019, 8, 21, 13, 31, 47, tzinfo=timezone(timedelta(0), '+0000'))
    assert booking.action == 'interested'


@pytest.mark.parametrize(('device', 'user', 'event'), [
    ('1234', '5555', '8888'),
    (Device.placeholder(1234), User.placeholder(5555), Event.placeholder(8888))
])
def test_create_booking(requests_mock, device, user, event):

    mock_responses = (
        ('POST', 'https://' + TEST_API_DOMAIN + '/v4/bookings', 'mock_responses/ls_api/create_booking.json', 200),
    )
    configure_mock_responses(requests_mock, mock_responses, FIXTURES_DIR, CONTENT_TYPE)

    resource_client = LiveStyledResourceClient(TEST_API_DOMAIN, 'bar')
    resource_client.create_booking(
        Booking.create_new(
            type='manual',
            device=device,
            user=user,
            event=event,
            action='going'
        )
    )

    assert len(requests_mock.request_history) == 1
    assert requests_mock.request_history[0].method == 'POST'
    assert requests_mock.request_history[0].url == 'https://' + TEST_API_DOMAIN + '/v4/bookings'
    assert json.loads(requests_mock.request_history[0].body) == {
        'action': 'going',
        'event': '/v4/events/8888',
        'device': '/v4/devices/1234',
        'type': 'manual',
        'user': '/v4/users/5555'
    }
