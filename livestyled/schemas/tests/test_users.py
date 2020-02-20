import os

from livestyled.schemas.user import UserSchema


FIXTURES_DIR = os.path.join(os.path.dirname(__file__), 'fixtures')
TEST_API_DOMAIN = 'test.livestyled.com'
CONTENT_TYPE = 'application/ld+json'


def test_deserialize_user():
    with open(os.path.join(FIXTURES_DIR, 'example_user.json'), 'r') as fixture_file:
        user = fixture_file.read()
        deserialized_user = UserSchema().loads(user)
        assert deserialized_user == {
            'auth_type': 'AXS',
            'email': 'reuben.gow+axs2@livestyled.com',
            'id': 278405,
            'user_info': {
                'first_name': 'Reuben',
                'last_name': 'Gow'
            }
        }