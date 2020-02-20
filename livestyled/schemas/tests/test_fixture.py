from datetime import datetime, timedelta, timezone
import os

from livestyled.schemas.fixture import FixtureSchema


FIXTURES_DIR = os.path.join(os.path.dirname(__file__), 'fixtures')
TEST_API_DOMAIN = 'test.livestyled.com'
CONTENT_TYPE = 'application/ld+json'


def test_deserialize_fixture():
    with open(os.path.join(FIXTURES_DIR, 'example_fixture.json'), 'r') as fixture_file:
        fixture = fixture_file.read()
        deserialized_fixture = FixtureSchema().loads(fixture)
        assert deserialized_fixture == {
            'away_id': 61,
            'away_score': {'goals': 1, 'penalties': None},
            'competition_id': 6,
            'home_id': 6,
            'home_score': {'goals': 1, 'penalties': None},
            'id': 198,
            'is_fulltime': False,
            'is_terminated': False,
            'season_id': 2,
            'start_at': datetime(2020, 8, 28, 9, 46, 2, tzinfo=timezone(timedelta(0), '+0000')),
            'venue_id': 5
        }


def test_serialize_fixture():
    serialized_fixture = FixtureSchema().dump(
        {
            'away_id': 61,
            'away_score': {'goals': 1, 'penalties': None},
            'competition_id': 6,
            'home_id': 6,
            'home_score': {'goals': 1, 'penalties': None},
            'id': 198,
            'is_fulltime': False,
            'is_terminated': False,
            'season_id': 2,
            'start_at': datetime(2020, 8, 28, 9, 46, 2, tzinfo=timezone(timedelta(0), '+0000')),
            'venue_id': 5
        }
    )
    assert serialized_fixture == {
        'away': '/v4/teams/61',
        'awayScore': {'goals': 1, 'penalties': None},
        'competition': '/v4/competitions/6',
        'home': '/v4/teams/6',
        'homeScore': {'goals': 1, 'penalties': None},
        'isFullTime': False,
        'isTerminated': False,
        'season': '/v4/seasons/2',
        'sportVenue': '/v4/venues/5',
        'startAt': '2020-08-28T09:46:02+00:00'
    }