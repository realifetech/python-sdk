from datetime import datetime, timedelta, timezone

from livestyled.models.fixture import Fixture
from livestyled.schemas.fixture import FixtureSchema


def test_create_fixture_from_deserialized():
    deserialized_fixture = {
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
        'venue_id': 5,
        'external_id': None,
        'status': 'Active',
        'url': {
            'url': 'https://test.com',
            'is_enabled': True,
            'title': 'TEST'
        }
    }
    fixture = Fixture(**deserialized_fixture)
    assert fixture


def test_serialize_fixture():
    deserialized_fixture = {
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
        'venue_id': 5,
        'external_id': None,
        'status': 'Active',
        'url': {
            'url': 'https://test.com',
            'is_enabled': True,
            'title': 'TEST'
        }
    }
    fixture = Fixture(**deserialized_fixture)
    serialized_fixture = FixtureSchema().dump(fixture)
    assert serialized_fixture
    assert serialized_fixture['competition'] == '/v4/competitions/6'
    assert serialized_fixture['url'] == {
        'url': 'https://test.com',
        'is_enabled': True,
        'title': 'TEST'
    }
