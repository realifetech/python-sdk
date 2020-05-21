from datetime import datetime, timedelta, timezone
import os

from livestyled.schemas.ticket import TicketSchema


FIXTURES_DIR = os.path.join(os.path.dirname(__file__), 'fixtures')
TEST_API_DOMAIN = 'test.livestyled.com'


def test_deserialize_ticket():
    with open(os.path.join(FIXTURES_DIR, 'example_ticket.json'), 'r') as fixture_file:
        ticket = fixture_file.read()
        deserialized_ticket = TicketSchema().loads(ticket)
        assert deserialized_ticket == {
            'barcode': None,
            'can_share': True,
            'client_email': 'test@livestyled.com',
            'client_name': None,
            'created_at': datetime(2019, 5, 16, 15, 31, 45, tzinfo=timezone(timedelta(0), '+0000')),
            'entrance': None,
            'external_customer_ref': None,
            'external_event_id': None,
            'external_ticket_id': '99999999',
            'id': 44,
            'parent_ticket': None,
            'premium': False,
            'price': 199,
            'price_code': None,
            'qr_code_url': '',
            'redeemer_email': None,
            'redeemer_id': None,
            'row': 'U',
            'seat': '1',
            'section': '128',
            'sector_name': None,
            'session_date': datetime(2020, 12, 24, 0, 0, tzinfo=timezone(timedelta(0), '+0000')),
            'share_code': None,
            'share_link': None,
            'shared_at': None,
            'sharer_email': None,
            'sharer_id': None,
            'status': 'active',
            'title': '128_U_1',
            'updated_at': datetime(2019, 5, 24, 12, 41, 22, tzinfo=timezone(timedelta(0), '+0000')),
            'user_id': None,
            'venue_name': None,
            'venue_room': None,
            'redeemed_at': None,
            'legal_long_text': 'this is the legal long text this is the legal long text '
                     'this is the legal long text this is the legal long text '
                     'this is the legal long text this is the legal long text '
                     'this is the legal long text this is the legal long text '
                     'this is the legal long text this is the legal long text '
                     'this is the legal long text this is the legal long text '
                     'this is the legal long text this is the legal long text',
            'legal_short_text': 'More information or questions regarding the ADA ticket',
            'map_url': None,
        }


def test_deserialize_ticket_shared():
    with open(os.path.join(FIXTURES_DIR, 'example_ticket_shared.json'), 'r') as fixture_file:
        ticket = fixture_file.read()
        deserialized_ticket = TicketSchema().loads(ticket)
        assert deserialized_ticket == {
            'barcode': None,
            'can_share': True,
            'client_email': 'test@livestyled.com',
            'client_name': None,
            'created_at': datetime(2019, 5, 16, 15, 31, 45, tzinfo=timezone(timedelta(0), '+0000')),
            'entrance': None,
            'external_customer_ref': None,
            'external_event_id': None,
            'external_ticket_id': '99999999',
            'id': 44,
            'parent_ticket': None,
            'premium': False,
            'price': 199,
            'price_code': None,
            'qr_code_url': '',
            'redeemer_email': None,
            'redeemer_id': None,
            'row': 'U',
            'seat': '1',
            'section': '128',
            'sector_name': None,
            'session_date': datetime(2020, 12, 24, 0, 0, tzinfo=timezone(timedelta(0), '+0000')),
            'share_code': 'ABCDEF12345',
            'share_link': None,
            'shared_at': datetime(2019, 5, 24, 12, 41, 22, tzinfo=timezone(timedelta(0), '+0000')),
            'sharer_email': 'test@livestyled.com',
            'sharer_id': None,
            'status': 'shared',
            'title': '128_U_1',
            'updated_at': datetime(2019, 5, 24, 12, 41, 22, tzinfo=timezone(timedelta(0), '+0000')),
            'user_id': None,
            'venue_name': None,
            'venue_room': None,
            'redeemed_at': None,
            'legal_long_text': None,
            'legal_short_text': None,
            'map_url': None
        }


def test_deserialize_ticket_shared_redeemed():
    with open(os.path.join(FIXTURES_DIR, 'example_ticket_shared_redeemed.json'), 'r') as fixture_file:
        ticket = fixture_file.read()
        deserialized_ticket = TicketSchema().loads(ticket)
        assert deserialized_ticket == {
            'barcode': None,
            'can_share': True,
            'client_email': 'test@livestyled.com',
            'client_name': None,
            'created_at': datetime(2019, 5, 16, 15, 31, 45, tzinfo=timezone(timedelta(0), '+0000')),
            'entrance': None,
            'external_customer_ref': None,
            'external_event_id': None,
            'external_ticket_id': '99999999',
            'id': 44,
            'parent_ticket': None,
            'premium': False,
            'price': 199,
            'price_code': None,
            'qr_code_url': '',
            'redeemer_email': 'someoneelse@livestyled.com',
            'redeemer_id': 1234,
            'row': 'U',
            'seat': '1',
            'section': '128',
            'sector_name': None,
            'session_date': datetime(2020, 12, 24, 0, 0, tzinfo=timezone(timedelta(0), '+0000')),
            'share_code': 'ABCDEF12345',
            'share_link': None,
            'shared_at': datetime(2019, 5, 24, 12, 41, 22, tzinfo=timezone(timedelta(0), '+0000')),
            'sharer_email': 'test@livestyled.com',
            'sharer_id': None,
            'status': 'redeemed',
            'title': '128_U_1',
            'updated_at': datetime(2019, 5, 24, 13, 41, 22, tzinfo=timezone(timedelta(0), '+0000')),
            'user_id': None,
            'venue_name': None,
            'venue_room': None,
            'redeemed_at': datetime(2019, 5, 24, 13, 41, 22, tzinfo=timezone(timedelta(0), '+0000')),
            'legal_long_text': None,
            'legal_short_text': None,
            'map_url': None,
        }
