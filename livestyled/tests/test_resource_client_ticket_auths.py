import json
import os

from livestyled.models.ticket_auth import TicketAuth
from livestyled.models.ticket_integration import TicketIntegration
from livestyled.models.user import UserEmail
from livestyled.resource_client import LiveStyledResourceClient
from livestyled.tests.utils import configure_mock_responses

FIXTURES_DIR = os.path.join(os.path.dirname(__file__), 'fixtures')
TEST_API_DOMAIN = 'test.livestyled.com'
CONTENT_TYPE = 'application/ld+json'


def test_get_ticket_auths(requests_mock):
    mock_responses = (
        ('GET', 'https://' + TEST_API_DOMAIN + '/v4/ticket_auths', 'mock_responses/ls_api/ticket_auth_list.json', 200),
    )
    configure_mock_responses(requests_mock, mock_responses, FIXTURES_DIR, CONTENT_TYPE)

    resource_client = LiveStyledResourceClient(TEST_API_DOMAIN, 'bar')
    ticket_auths = list(resource_client.get_ticket_auths())
    assert ticket_auths
    assert isinstance(ticket_auths[0], TicketAuth)
    assert ticket_auths[0].id == 1038
    assert isinstance(ticket_auths[0].user_email, UserEmail)
    assert ticket_auths[0].user_email.id == 330325
    assert ticket_auths[0].user_email.valid is True
    assert ticket_auths[0].user_email.email == 'amy.keane+verificatintest@livestyled.com'
    assert isinstance(ticket_auths[0].ticket_integration, TicketIntegration)
    assert ticket_auths[0].ticket_integration.id == 40
    assert ticket_auths[0].client_email == 'amy.keane+verificatintest@livestyled.com'
    assert ticket_auths[0].client_id == '129494829'


def test_get_ticket_auths_filtering(requests_mock):
    mock_responses = (
        ('GET', 'https://' + TEST_API_DOMAIN + '/v4/ticket_auths?userEmail.email=amy.keane%2Bverificatintest%40livestyled.com', 'mock_responses/ls_api/ticket_auth_list_filtered.json', 200),
    )
    configure_mock_responses(requests_mock, mock_responses, FIXTURES_DIR, CONTENT_TYPE)

    resource_client = LiveStyledResourceClient(TEST_API_DOMAIN, 'bar')
    ticket_auths = list(resource_client.get_ticket_auths(user_email_address='amy.keane+verificatintest@livestyled.com'))
    assert ticket_auths
    assert isinstance(ticket_auths[0], TicketAuth)
    assert ticket_auths[0].id == 1038
    assert isinstance(ticket_auths[0].user_email, UserEmail)
    assert ticket_auths[0].user_email.id == 330325
    assert ticket_auths[0].user_email.valid is True
    assert ticket_auths[0].user_email.email == 'amy.keane+verificatintest@livestyled.com'
    assert isinstance(ticket_auths[0].ticket_integration, TicketIntegration)
    assert ticket_auths[0].ticket_integration.id == 40
    assert ticket_auths[0].client_email == 'amy.keane+verificatintest@livestyled.com'
    assert ticket_auths[0].client_id == '129494829'


def test_update_ticket_auth(requests_mock):
    mock_responses = (
        ('PATCH', 'https://' + TEST_API_DOMAIN + '/v4/ticket_auths/1038', 'mock_responses/ls_api/ticket_auth_updated.json', 200),
    )
    configure_mock_responses(requests_mock, mock_responses, FIXTURES_DIR, CONTENT_TYPE)

    resource_client = LiveStyledResourceClient(TEST_API_DOMAIN, 'bar')
    resource_client.update_ticket_auth(
        TicketAuth.placeholder(1038),
        {
            'client_id': '99999'
        }
    )
    assert requests_mock.request_history[0].method == 'PATCH'
    assert json.loads(requests_mock.request_history[0].body) == {
        'clientId': '99999'
    }
