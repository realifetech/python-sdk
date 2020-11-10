from datetime import datetime, timedelta, timezone
import os

from livestyled.schemas.push_broadcast import PushBroadcastSchema


FIXTURES_DIR = os.path.join(os.path.dirname(__file__), 'fixtures')
TEST_API_DOMAIN = 'test.livestyled.com'


def test_deserialize_league_table():
    with open(os.path.join(FIXTURES_DIR, 'push_broadcast.json'), 'r') as fixture_file:
        push_broadcast = fixture_file.read()
        deserialized_push_broadcast = PushBroadcastSchema().loads(push_broadcast)
        assert deserialized_push_broadcast == {
            'created_at': datetime(2020, 2, 26, 23, 0, 20, tzinfo=timezone(timedelta(0), '+0000')),
            'deep_link': 'myapp://main/home',
            'delivered': 0,
            'id': 52,
            'message': 'This is not a test',
            'message_id': 'f87efee3-3f01-5ca5-b05a-1234567',
            'title': 'Push Notification',
            'ttl': 0,
            'updated_at': datetime(2020, 2, 26, 23, 0, 20, tzinfo=timezone(timedelta(0), '+0000'))
        }
