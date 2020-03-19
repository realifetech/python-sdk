import os

import pytest

from livestyled.models.team import Team
from livestyled.resource_client import LiveStyledResourceClient
from livestyled.tests.utils import configure_mock_responses

FIXTURES_DIR = os.path.join(os.path.dirname(__file__), 'fixtures')
TEST_API_DOMAIN = 'test.livestyled.com'
CONTENT_TYPE = 'application/ld+json'


def test_get_team_by_external_id(requests_mock):
    mock_responses = (
        ('GET', 'https://' + TEST_API_DOMAIN + '/v4/teams?externalId=t3', 'mock_responses/ls_api/teams_external_id_t3.json', 200),
    )
    configure_mock_responses(requests_mock, mock_responses, FIXTURES_DIR, CONTENT_TYPE)

    resource_client = LiveStyledResourceClient(TEST_API_DOMAIN, 'bar')
    teams = list(resource_client.get_teams(external_id='t3'))
    assert teams
    team = teams[0]
    assert team.name == 'Arsenal'
    assert team.short_name == 'ARS'
    assert team.light_crest_url == 'https://apiv3-dev.s3.eu-west-1.amazonaws.com/27/team/arsenal-300x300.png'
    assert team.dark_crest_url == 'https://apiv3-dev.s3.eu-west-1.amazonaws.com/27/team/arsenal-300x300.png'
    assert team.external_id == 't3'


def test_get_team_by_id(requests_mock):
    mock_responses = (
        ('GET', 'https://' + TEST_API_DOMAIN + '/v4/teams/6', 'mock_responses/ls_api/team_6.json', 200),
    )
    configure_mock_responses(requests_mock, mock_responses, FIXTURES_DIR, CONTENT_TYPE)

    resource_client = LiveStyledResourceClient(TEST_API_DOMAIN, 'bar')
    team = resource_client.get_team(6)
    assert team.name == 'LiveStyled'
    assert team.short_name == 'LS'
    assert team.light_crest_url == 'https://apiv3.s3.eu-west-1.amazonaws.com/team/Logo_White_nontext.png'
    assert team.dark_crest_url == 'https://apiv3.s3.eu-west-1.amazonaws.com/team/Logo_Purple_notext.png'
    assert team.external_id is None


def test_create_team(requests_mock):
    team = Team.create_new(
        external_id='testteam1',
        name='Test Team',
        short_name='TT',
        light_crest_url='http://www.images.com/image1.jpg',
        dark_crest_url='http://www.images.com/image2.jpg'
    )
    mock_responses = (
        ('POST', 'https://' + TEST_API_DOMAIN + '/v4/teams', 'mock_responses/ls_api/create_team.json', 200),
    )
    configure_mock_responses(requests_mock, mock_responses, FIXTURES_DIR, CONTENT_TYPE)

    resource_client = LiveStyledResourceClient(TEST_API_DOMAIN, 'bar')
    created_team = resource_client.create_team(team)
    assert created_team
    assert created_team.id == 999

    for request in requests_mock.request_history:
        if request.method.upper() == 'POST' and request.url == 'https://' + TEST_API_DOMAIN + '/v4/teams':
            actual_payload = request.json()

            assert actual_payload == {
                'name': 'Test Team',
                'shortName': 'TT',
                'lightCrestUrl': 'http://www.images.com/image1.jpg',
                'darkCrestUrl': 'http://www.images.com/image2.jpg',
                'externalId': 'testteam1'
            }


def test_create_team_with_id(requests_mock):
    team = Team(
        id=1,
        external_id='testteam1',
        name='Test Team',
        short_name='TT',
        light_crest_url='http://www.images.com/image1.jpg',
        dark_crest_url='http://www.images.com/image2.jpg',
    )

    resource_client = LiveStyledResourceClient(TEST_API_DOMAIN, 'bar')

    with pytest.raises(ValueError, match='Cannot create a Team with an ID'):
        resource_client.create_team(team)


def test_update_team(requests_mock):
    team = Team(
        id=1,
        external_id='testteam1',
        name='Test Team',
        short_name='TT',
        light_crest_url='http://www.images.com/image1.jpg',
        dark_crest_url='http://www.images.com/image2.jpg',
    )

    resource_client = LiveStyledResourceClient(TEST_API_DOMAIN, 'bar')
    mock_responses = (
        ('PATCH', 'https://' + TEST_API_DOMAIN + '/v4/teams/1', 'mock_responses/ls_api/updated_team.json', 200),
    )
    configure_mock_responses(requests_mock, mock_responses, FIXTURES_DIR, CONTENT_TYPE)

    updated_team = resource_client.update_team(team, {'name': 'New Name'})

    for request in requests_mock.request_history:
        if request.method.upper() == 'PATCH' and request.url == 'https://' + TEST_API_DOMAIN + '/v4/teams/1':
            actual_payload = request.json()

            assert actual_payload == {
                'name': 'New Name'
            }

    assert updated_team.name == 'New Name'
    assert updated_team.id == 1
    assert updated_team.external_id == 'testteam1'
    assert updated_team.short_name == 'TT'
    assert updated_team.light_crest_url == 'http://www.images.com/image1.jpg'
    assert updated_team.dark_crest_url == 'http://www.images.com/image2.jpg'
