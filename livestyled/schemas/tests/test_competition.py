import os

from livestyled.schemas.competition import CompetitionSchema


FIXTURES_DIR = os.path.join(os.path.dirname(__file__), 'fixtures')
TEST_API_DOMAIN = 'test.livestyled.com'
CONTENT_TYPE = 'application/ld+json'


def test_deserialize_competition():
    with open(os.path.join(FIXTURES_DIR, 'example_competition.json'), 'r') as fixture_file:
        competition = fixture_file.read()
        deserialized_competition = CompetitionSchema().loads(competition)
        assert deserialized_competition == {
            'id': 58,
            'name': 'MLS Regular Season - West Conference',
            'status': 'ACTIVE',
            'external_id': '98',
            'logo_url': None,
            'sort_id': 0
        }
