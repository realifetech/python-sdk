import os

import pytest

from livestyled.client import LiveStyledAPIClient
from livestyled.tests.utils import configure_mock_responses

FIXTURES_DIR = os.path.join(os.path.dirname(__file__), 'fixtures')
TEST_API_DOMAIN = 'test.livestyled.com'
CONTENT_TYPE = 'application/ld+json'


@pytest.fixture(scope='session')
def test_client():
    return LiveStyledAPIClient(
        api_domain=TEST_API_DOMAIN,
        api_key='thisisjustatest'
    )


def test_client_can_get_app_by_id(requests_mock, test_client):

    mock_responses = (
        ('GET', 'https://' + TEST_API_DOMAIN + '/v4/apps/1', 'mock_responses/ls_api/app_1.json', 200),
    )
    configure_mock_responses(requests_mock, mock_responses, FIXTURES_DIR, CONTENT_TYPE)

    app = test_client.get_app(1)
    assert app == {
        'email': None,
        'roles': [
            'ROLE_APP'
        ],
        'password': 'APPID',
        'salt': None,
        'username': 'TestAppUser1',
        'code': 'TARENA1',
        'token': 'token',
        'id': 1,
        'name': 'Test Arena 1',
        'api_keys': [
            'APPID'
        ],
        'timezone': 'Europe/London',
        'google_api_key': None,
        'payment_gateway': 'PAYMENTGW1',
        'venues': [],
        'sender_email': 'support@livestyed.net',
        'deeplink_namespace': '',
        'merchant_accounts': [],
        'title': 'Test Arena 1',
        'status': 'DISABLED',
        'currency': {
            'id': 1,
            'title': 'Pound',
            'isoCode': 'GBP',
            'sign': '£',
            'updatedAt': '2016-08-09T10:49:34+00:00',
            'createdAt': '2016-08-09T10:49:34+00:00',
            '__initializer__': None,
            '__cloner__': None,
            '__isInitialized__': True
        },
        'cohorts': []
    }


def test_client_can_get_list_of_apps(requests_mock, test_client):

    mock_responses = (
        ('GET', 'https://' + TEST_API_DOMAIN + '/v4/apps', 'mock_responses/ls_api/apps_list_page_1.json', 200),
        ('GET', 'https://' + TEST_API_DOMAIN + '/v4/apps?page=2', 'mock_responses/ls_api/apps_list_page_2.json', 200),
    )
    configure_mock_responses(requests_mock, mock_responses, FIXTURES_DIR, CONTENT_TYPE)

    apps = test_client.get_apps()
    assert sum(1 for _ in apps) == 4
