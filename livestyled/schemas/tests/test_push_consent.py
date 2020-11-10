from datetime import datetime, timedelta, timezone
import os

from livestyled.schemas.push_consent import PushConsentSchema


FIXTURES_DIR = os.path.join(os.path.dirname(__file__), 'fixtures')
TEST_API_DOMAIN = 'test.livestyled.com'


def test_deserialize_league_table():
    with open(os.path.join(FIXTURES_DIR, 'push_consent.json'), 'r') as fixture_file:
        push_consent = fixture_file.read()
        deserialized_push_consent = PushConsentSchema().loads(push_consent)
        assert deserialized_push_consent == {
            'created_at': datetime(2020, 2, 14, 10, 20, 5, tzinfo=timezone(timedelta(0), '+0000')),
            'label': 'Matchday Alerts',
            'sort_id': 1,
            'title': 'Matchday Alerts',
            'translations': [],
            'type': 'eventReminders',
            'id': 60,
            'updated_at': datetime(2020, 2, 14, 10, 20, 5, tzinfo=timezone(timedelta(0), '+0000'))
        }
