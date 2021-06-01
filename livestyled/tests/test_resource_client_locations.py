import os

from livestyled.models.location import Location, LocationCoordinates
from livestyled.resource_client import LiveStyledResourceClient
from livestyled.tests.utils import configure_mock_responses

FIXTURES_DIR = os.path.join(os.path.dirname(__file__), 'fixtures')
TEST_API_DOMAIN = 'test.livestyled.com'
CONTENT_TYPE = 'application/ld+json'


def test_get_locations(requests_mock):
    mock_responses = (
        ('GET', 'https://' + TEST_API_DOMAIN + '/v4/user_management/locations', 'mock_responses/ls_api/user_management/locations.json', 200),
    )
    configure_mock_responses(requests_mock, mock_responses, FIXTURES_DIR, CONTENT_TYPE)

    resource_client = LiveStyledResourceClient(TEST_API_DOMAIN, 'bar')
    locations = list(resource_client.get_locations())
    assert locations
    assert len(locations) == 19
    assert isinstance(locations[0], Location)
    assert locations[0].id == 1
    assert locations[0].listed is True
    assert locations[0].name == 'Berlin'
    assert locations[0].coordinates.lat == 52.5200
    assert locations[0].coordinates.lon == 13.4050
    assert locations[0].polygon is None
    assert locations[0].sort_id == 10
    assert locations[0].external_id == ''

    assert locations[2].id == 3
    assert locations[2].status == 'active'
    assert locations[2].listed is True
    assert locations[2].name == 'London'
    assert locations[2].coordinates.lat == 51.5074
    assert locations[2].coordinates.lon == 0.1278
    assert locations[2].polygon.coordinates == [
        LocationCoordinates(51.687030937462666, -0.1373291015625),
        LocationCoordinates(51.7151177895987, -0.27191162109374994),
        LocationCoordinates(51.72022261695929, -0.416107177734375),
        LocationCoordinates(51.62142713341988, -0.536956787109375),
    ]

    assert locations[3].id == 4
    assert locations[3].status == 'active'
    assert locations[3].listed is False
    assert locations[3].name == 'LS Office CO'
    assert locations[3].coordinates.lat == 51.5413393
    assert locations[3].coordinates.lon == -0.09543170000000001
    assert locations[3].polygon.coordinates == [
        LocationCoordinates(51.543792920127274, -0.10062575340270996),
        LocationCoordinates(51.542838751511205, -0.10001420974731445),
        LocationCoordinates(51.54066343916916, -0.09590506553649901),
        LocationCoordinates(51.543586074083876, -0.09056210517883301),
        LocationCoordinates(51.54612821344662, -0.09384512901306152),
        LocationCoordinates(51.543792920127274, -0.10062575340270996),
    ]
    assert locations[3].external_id is None
