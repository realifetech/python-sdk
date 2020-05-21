from datetime import datetime, timedelta, timezone
import os

from livestyled.models.ticket import Ticket
from livestyled.models.user import User
from livestyled.resource_client import LiveStyledResourceClient
from livestyled.tests.utils import configure_mock_responses

FIXTURES_DIR = os.path.join(os.path.dirname(__file__), 'fixtures')
TEST_API_DOMAIN = 'test.livestyled.com'
CONTENT_TYPE = 'application/ld+json'


def test_get_ticket(requests_mock):
    mock_responses = (
        ('GET', 'https://' + TEST_API_DOMAIN + '/v4/tickets/44', 'mock_responses/ls_api/example_ticket.json', 200),
    )
    configure_mock_responses(requests_mock, mock_responses, FIXTURES_DIR, CONTENT_TYPE)

    resource_client = LiveStyledResourceClient(TEST_API_DOMAIN, 'bar')
    ticket = resource_client.get_ticket(44)
    assert ticket
    assert isinstance(ticket, Ticket)
    assert ticket.id == 44
    assert ticket.external_ticket_id == '99999999'
    assert ticket.seat == '1'
    assert ticket.qr_code_url == ''
    assert ticket.session_date == datetime(2020, 12, 24, 0, 0, tzinfo=timezone(timedelta(0), '+0000'))
    assert ticket.barcode is None
    assert ticket.can_share is True
    assert ticket.client_email == 'test@livestyled.com'
    assert ticket.client_name is None
    assert ticket.created_at == datetime(2019, 5, 16, 15, 31, 45, tzinfo=timezone(timedelta(0), '+0000'))
    assert ticket.entrance is None
    assert ticket.external_customer_ref is None
    assert ticket.external_event_id is None
    assert ticket.parent_ticket is None
    assert ticket.premium is False
    assert ticket.price == 199
    assert ticket.price_code is None
    assert ticket.redeemer_email is None
    assert ticket.redeemer_id is None
    assert ticket.redeemer is None
    assert ticket.row == 'U'
    assert ticket.section == '128'
    assert ticket.sector_name is None
    assert ticket.share_code is None
    assert ticket.share_link is None
    assert ticket.shared_at is None
    assert ticket.sharer_email is None
    assert ticket.updated_at == datetime(2019, 5, 24, 12, 41, 22, tzinfo=timezone(timedelta(0), '+0000'))
    assert ticket.user_id is None
    assert ticket.user is None
    assert ticket.venue_name is None
    assert ticket.venue_room is None
    assert ticket.redeemed_at is None


def test_get_ticket_shared(requests_mock):
    mock_responses = (
        ('GET', 'https://' + TEST_API_DOMAIN + '/v4/tickets/44', 'mock_responses/ls_api/example_ticket_shared.json', 200),
    )
    configure_mock_responses(requests_mock, mock_responses, FIXTURES_DIR, CONTENT_TYPE)

    resource_client = LiveStyledResourceClient(TEST_API_DOMAIN, 'bar')
    ticket = resource_client.get_ticket(44)
    assert ticket
    assert isinstance(ticket, Ticket)
    assert ticket.id == 44
    assert ticket.external_ticket_id == '99999999'
    assert ticket.seat == '1'
    assert ticket.qr_code_url == ''
    assert ticket.session_date == datetime(2020, 12, 24, 0, 0, tzinfo=timezone(timedelta(0), '+0000'))
    assert ticket.barcode is None
    assert ticket.can_share is True
    assert ticket.client_email == 'test@livestyled.com'
    assert ticket.client_name is None
    assert ticket.created_at == datetime(2019, 5, 16, 15, 31, 45, tzinfo=timezone(timedelta(0), '+0000'))
    assert ticket.entrance is None
    assert ticket.external_customer_ref is None
    assert ticket.external_event_id is None
    assert ticket.parent_ticket is None
    assert ticket.premium is False
    assert ticket.price == 199
    assert ticket.price_code is None
    assert ticket.redeemer_email is None
    assert ticket.redeemer_id is None
    assert ticket.redeemer is None
    assert ticket.row == 'U'
    assert ticket.section == '128'
    assert ticket.sector_name is None
    assert ticket.share_code == 'ABCDEF12345'
    assert ticket.share_link is None
    assert ticket.shared_at == datetime(2019, 5, 24, 12, 41, 22, tzinfo=timezone(timedelta(0), '+0000'))
    assert ticket.sharer_email == 'test@livestyled.com'
    assert ticket.updated_at == datetime(2019, 5, 24, 12, 41, 22, tzinfo=timezone(timedelta(0), '+0000'))
    assert ticket.user_id is None
    assert ticket.user is None
    assert ticket.venue_name is None
    assert ticket.venue_room is None
    assert ticket.redeemed_at is None


def test_get_ticket_shared_redeemed(requests_mock):
    mock_responses = (
        ('GET', 'https://' + TEST_API_DOMAIN + '/v4/tickets/44', 'mock_responses/ls_api/example_ticket_shared_redeemed.json', 200),
    )
    configure_mock_responses(requests_mock, mock_responses, FIXTURES_DIR, CONTENT_TYPE)

    resource_client = LiveStyledResourceClient(TEST_API_DOMAIN, 'bar')
    ticket = resource_client.get_ticket(44)
    assert ticket
    assert isinstance(ticket, Ticket)
    assert ticket.id == 44
    assert ticket.external_ticket_id == '99999999'
    assert ticket.seat == '1'
    assert ticket.qr_code_url == ''
    assert ticket.session_date == datetime(2020, 12, 24, 0, 0, tzinfo=timezone(timedelta(0), '+0000'))
    assert ticket.barcode is None
    assert ticket.can_share is True
    assert ticket.client_email == 'test@livestyled.com'
    assert ticket.client_name is None
    assert ticket.created_at == datetime(2019, 5, 16, 15, 31, 45, tzinfo=timezone(timedelta(0), '+0000'))
    assert ticket.entrance is None
    assert ticket.external_customer_ref is None
    assert ticket.external_event_id is None
    assert ticket.parent_ticket is None
    assert ticket.premium is False
    assert ticket.price == 199
    assert ticket.price_code is None
    assert ticket.redeemer_email == 'someoneelse@livestyled.com'
    assert ticket.redeemer_id == 1234
    assert isinstance(ticket.redeemer, User)
    assert ticket.redeemer.id == 1234
    assert ticket.row == 'U'
    assert ticket.section == '128'
    assert ticket.sector_name is None
    assert ticket.share_code == 'ABCDEF12345'
    assert ticket.share_link is None
    assert ticket.shared_at == datetime(2019, 5, 24, 12, 41, 22, tzinfo=timezone(timedelta(0), '+0000'))
    assert ticket.sharer_email == 'test@livestyled.com'
    assert ticket.updated_at == datetime(2019, 5, 24, 13, 41, 22, tzinfo=timezone(timedelta(0), '+0000'))
    assert ticket.user_id is None
    assert ticket.user is None
    assert ticket.venue_name is None
    assert ticket.venue_room is None
    assert ticket.redeemed_at == datetime(2019, 5, 24, 13, 41, 22, tzinfo=timezone(timedelta(0), '+0000'))
