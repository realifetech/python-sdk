import os
from typing import List

from livestyled.models import Banner, BannerTranslation
from livestyled.resource_client import LiveStyledResourceClient
from livestyled.tests.utils import configure_mock_responses


FIXTURES_DIR = os.path.join(os.path.dirname(__file__), 'fixtures')
TEST_API_DOMAIN = 'test.livestyled.com'
CONTENT_TYPE = 'application/ld+json'

REQUEST_BASE_URL = 'https://' + TEST_API_DOMAIN + '/v4/{}'


def test_get_banners(requests_mock):
    mock_file = 'mock_responses/ls_api/content_management/banners.json'
    mock_responses = (
        ('GET', REQUEST_BASE_URL.format('content_management/banners'), mock_file, 200),
    )
    configure_mock_responses(requests_mock, mock_responses, FIXTURES_DIR, CONTENT_TYPE)

    resource_client = LiveStyledResourceClient(TEST_API_DOMAIN, 'bar')
    banners = resource_client.get_banners()
    current_banner = next(banners)
    assert isinstance(current_banner, Banner)
    assert isinstance(current_banner.translations, List)
    assert isinstance(current_banner.translations[0], BannerTranslation)


def test_get_banner(requests_mock):
    mock_file = 'mock_responses/ls_api/content_management/item_banner.json'
    collection_endpoint = REQUEST_BASE_URL.format('content_management/banners/1')
    mock_responses = (
        ('GET', collection_endpoint, mock_file, 200),
    )

    configure_mock_responses(requests_mock, mock_responses, FIXTURES_DIR, CONTENT_TYPE)

    resource_client = LiveStyledResourceClient(TEST_API_DOMAIN, 'bar')
    banner = resource_client.get_banner(id=1)
    assert isinstance(banner, Banner)
    assert isinstance(banner.translations, List)
