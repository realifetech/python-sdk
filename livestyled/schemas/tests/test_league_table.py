import os

from livestyled.schemas.league_table import LeagueTableSchema


FIXTURES_DIR = os.path.join(os.path.dirname(__file__), 'fixtures')
TEST_API_DOMAIN = 'test.livestyled.com'


def test_deserialize_league_table():
    with open(os.path.join(FIXTURES_DIR, 'league_table.json'), 'r') as fixture_file:
        league_table = fixture_file.read()
        deserialized_league_table = LeagueTableSchema().loads(league_table)
        assert deserialized_league_table == {
            'id': 116,
            'team_id': 400,
            'external_id': '506208',
            'featured_team': False,
            'position': 12,
            'played': 2,
            'goals_for': 1,
            'goals_against': 5,
            'start_day_position': 12,
            'won': 0,
            'lost': 1,
            'drawn': 1,
            'goal_difference': -4,
            'points': 1,
            'competition_id': 58,
            'season_id': 9,
            'group_id': 5
        }
