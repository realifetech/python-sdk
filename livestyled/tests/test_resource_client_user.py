import datetime
import os

from livestyled.models.cohort import Cohort
from livestyled.models.user import User
from livestyled.resource_client import LiveStyledResourceClient
from livestyled.schemas.user import UserSchema
from livestyled.tests.utils import configure_mock_responses

FIXTURES_DIR = os.path.join(os.path.dirname(__file__), 'fixtures')
TEST_API_DOMAIN = 'test.livestyled.com'
CONTENT_TYPE = 'application/ld+json'


def test_get_user_by_id(requests_mock):
    mock_responses = (
        ('GET', 'https://' + TEST_API_DOMAIN + '/v4/users/1234', 'mock_responses/ls_api/user_1234.json', 200),
    )
    configure_mock_responses(requests_mock, mock_responses, FIXTURES_DIR, CONTENT_TYPE)

    resource_client = LiveStyledResourceClient(TEST_API_DOMAIN, 'bar')
    user = resource_client.get_user(1234)
    assert user
    assert isinstance(user, User)
    assert user.id == 1234
    assert user.email == 'bob.bobberson@test.com'
    assert user.auth_type == 'LOCAL'
    assert user.first_name == 'Bob'
    assert user.last_name == 'Bobberson'
    assert user.password is None
    assert set(user.cohorts) == {
        Cohort.placeholder(1),
        Cohort.placeholder(2),
        Cohort.placeholder(8)
    }
    assert user.user_info.first_name == 'Bob'
    assert user.user_info.last_name == 'Bobberson'
    assert user.user_info.dob == datetime.datetime(1992, 12, 6, 0, 0, tzinfo=datetime.timezone(datetime.timedelta(0), '+0000'))
    assert user.user_info.gender == 'MALE'
    assert len(user.magic_fields) == 1
    assert user.magic_fields[0].key == 'rtest'
    assert user.magic_fields[0].value == 'foobar'
    assert user.magic_fields[0].id == 52
    assert len(user.devices) == 1
    assert user.devices[0].id == 1753940
    assert user.devices[0].token == 'EEDF8B6C-4DD8-4D04-B5D6-D6AE62CD5146'
    assert user.devices[0].type == 'IOS'
    assert user.devices[0].consent.push_notification is True


def test_user_diff(requests_mock):
    mock_responses = (
        ('GET', 'https://' + TEST_API_DOMAIN + '/v4/users/1234', 'mock_responses/ls_api/user_1234.json', 200),
    )
    configure_mock_responses(requests_mock, mock_responses, FIXTURES_DIR, CONTENT_TYPE)

    resource_client = LiveStyledResourceClient(TEST_API_DOMAIN, 'bar')
    user1 = resource_client.get_user(1234)
    user2 = resource_client.get_user(1234)

    user2.user_info.first_name = 'Bobby'

    differences = user2.diff(user1)
    assert differences
    assert 'user_info' in differences

    serialised_differences = UserSchema(only=['user_info']).dump(differences)
    assert serialised_differences
    assert serialised_differences == {
        'userInfo': {
            'id': 37,
            'dob': '1992-12-06T00:00:00+00:00',
            'firstName': 'Bobby',
            'gender': 'MALE',
            'lastName': 'Bobberson',
            'phone': None
        }
    }
