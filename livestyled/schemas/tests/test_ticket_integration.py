import os

from livestyled.schemas.ticket_integration import TicketIntegrationSchema


FIXTURES_DIR = os.path.join(os.path.dirname(__file__), 'fixtures')
TEST_API_DOMAIN = 'test.livestyled.com'


def test_deserialize_ticket_integration():
    with open(os.path.join(FIXTURES_DIR, 'example_ticket_integration.json'), 'r') as fixture_file:
        ticket_integration = fixture_file.read()
        deserialized_ticket_integration = TicketIntegrationSchema().loads(ticket_integration)
        assert deserialized_ticket_integration == {
            'adapter': 'XXXXXXds',
            'auth_required': False,
            'can_share': False,
            'config_payload': None,
            'endpoint_url': 'XXXXXXsd',
            'id': 17,
            'default': False,
            'label': 'XXXXXXdsds',
            'login_request': 'XXXXXXXdsds',
            'module': 'SHARE',
            'name': 'SeatGeek',
        }
