from datetime import datetime, timedelta, timezone
import os

from livestyled.models import News
from livestyled.resource_client import LiveStyledResourceClient
from livestyled.tests.utils import configure_mock_responses

FIXTURES_DIR = os.path.join(os.path.dirname(__file__), 'fixtures')
TEST_API_DOMAIN = 'test.livestyled.com'
CONTENT_TYPE = 'application/ld+json'


def test_get_news_by_id(requests_mock):
    mock_responses = (
        ('GET', 'https://' + TEST_API_DOMAIN + '/v4/news/1234', 'mock_responses/ls_api/news_1234.json', 200),
    )
    configure_mock_responses(requests_mock, mock_responses, FIXTURES_DIR, CONTENT_TYPE)

    resource_client = LiveStyledResourceClient(TEST_API_DOMAIN, 'bar')
    news = resource_client.get_news_article(1234)
    assert isinstance(news, News)
    assert news.id == 1234
    assert news.title == 'Things happened'
    assert news.external_id == '50990'
    assert news.published_at == datetime(2020, 2, 23, 4, 56, 59, tzinfo=timezone(timedelta(0), '+0000'))
    assert news.headline == 'Some news'
    assert news.author is None
    assert news.updated_at == datetime(2020, 3, 18, 1, 15, 7, tzinfo=timezone(timedelta(0), '+0000'))
    assert news.media == {
        'type': 'EXTERNALVIDEO',
        'url': 'https://www.thenews.com/video',
    }


def test_get_news(requests_mock):
    mock_responses = (
        ('GET', 'https://' + TEST_API_DOMAIN + '/v4/news', 'mock_responses/ls_api/news.json', 200),
    )
    configure_mock_responses(requests_mock, mock_responses, FIXTURES_DIR, CONTENT_TYPE)

    resource_client = LiveStyledResourceClient(TEST_API_DOMAIN, 'bar')
    news = resource_client.get_news_articles()
    news = [n for n in news]
    assert len(news) == 2
    news.sort(key=lambda n: n.id)
    assert news[0].id == 1234
    assert news[1].id == 1235
