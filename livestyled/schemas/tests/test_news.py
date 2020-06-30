from datetime import datetime, timedelta, timezone
import os

from livestyled.schemas.news import NewsSchema


FIXTURES_DIR = os.path.join(os.path.dirname(__file__), 'fixtures')
TEST_API_DOMAIN = 'test.livestyled.com'


def test_deserialize_league_table():
    with open(os.path.join(FIXTURES_DIR, 'news.json'), 'r') as fixture_file:
        news = fixture_file.read()
        deserialized_news = NewsSchema().loads(news)
        assert deserialized_news == {
            'id': 6261,
            'author': None,
            'external_id': '50990',
            'headline': 'Some news',
            'image_url': 'https://image.livestyled.com/abcdefg',
            'media': {
                'type': 'EXTERNALVIDEO',
                'url': 'https://www.thenews.com/video',
                'thumbnail_url': None,
            },
            'published_at': datetime(2020, 2, 23, 4, 56, 59, tzinfo=timezone(timedelta(0), '+0000')),
            'title': 'Things happened',
            'updated_at': datetime(2020, 3, 18, 1, 15, 7, tzinfo=timezone(timedelta(0), '+0000')),
            'url': 'https://www.thenews.com'
        }
