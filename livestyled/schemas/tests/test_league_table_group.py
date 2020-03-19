import os

from livestyled.schemas.league_table import LeagueTableGroupSchema


FIXTURES_DIR = os.path.join(os.path.dirname(__file__), 'fixtures')
TEST_API_DOMAIN = 'test.livestyled.com'


def test_deserialize_league_table_group():
    with open(os.path.join(FIXTURES_DIR, 'league_table_group.json'), 'r') as fixture_file:
        league_table_group = fixture_file.read()
        deserialized_league_table_group = LeagueTableGroupSchema().loads(league_table_group)
        assert deserialized_league_table_group == {
            'id': 5,
            'reference': 'West',
            'title': 'Group West',
        }
