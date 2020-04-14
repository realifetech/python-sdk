from datetime import datetime, timedelta, timezone
import os

from livestyled.models.event import Event
from livestyled.resource_client import LiveStyledResourceClient
from livestyled.tests.utils import configure_mock_responses

FIXTURES_DIR = os.path.join(os.path.dirname(__file__), 'fixtures')
TEST_API_DOMAIN = 'test.livestyled.com'
CONTENT_TYPE = 'application/ld+json'


def test_get_events(requests_mock):
    mock_responses = (
        ('GET', 'https://' + TEST_API_DOMAIN + '/v4/events', 'mock_responses/ls_api/events_page1.json', 200),
        ('GET', 'https://' + TEST_API_DOMAIN + '/v4/events?page=2', 'mock_responses/ls_api/events_page2.json', 200),
    )
    configure_mock_responses(requests_mock, mock_responses, FIXTURES_DIR, CONTENT_TYPE)

    resource_client = LiveStyledResourceClient(TEST_API_DOMAIN, 'bar')
    events = list(resource_client.get_events())
    assert events
    assert len(events) == 31
    event = events[0]
    assert isinstance(event, Event)
    assert event.title == 'SABATON'
    assert event.status == 'ACTIVE'
    assert event.description == "Thirty-three drivers. 200 laps. 500 miles. One bottle of cold milk. The only thing missing from this magical Indianapolis 500 mix is you. Don't miss out on another incredible edition of \"The Greatest Spectacle in Racing.\""
    assert event.image_url == 'http://d255vb63773d25.cloudfront.net/-/media/IMS/events/schedule-images/indy-500/2020/Indy500.png?vs=1&d=20200326T144925Z'
    assert event.promoted is False
    assert event.created_at == datetime(2015, 7, 22, 17, 53, 56, tzinfo=timezone(timedelta(0), '+0000'))
    assert event.updated_at == datetime(2020, 4, 9, 15, 0, 42, tzinfo=timezone(timedelta(0), '+0000'))
    assert len(event.event_dates) == 1
    assert event.event_dates[0].id == 5448
    assert event.event_dates[0].start_at == datetime(2017, 3, 29, 16, 0, tzinfo=timezone(timedelta(0), '+0000'))
    assert event.event_dates[0].end_at == datetime(2017, 3, 29, 19, 0, tzinfo=timezone(timedelta(0), '+0000'))
    assert event.event_dates[0].general_ticket_url == 'https://www.ticketmaster.co.uk/Blue-tickets/artist/1843366'
    assert event.translations is None
