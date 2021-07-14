import os

from livestyled.models import Audience, FulfilmentPoint, FulfilmentPointCategory, FulfilmentPointTranslation
from livestyled.resource_client import LiveStyledResourceClient
from livestyled.tests.utils import configure_mock_responses

FIXTURES_DIR = os.path.join(os.path.dirname(__file__), 'fixtures')
TEST_API_DOMAIN = 'test.livestyled.com'
CONTENT_TYPE = 'application/ld+json'


def test_get_fulfilment_points(requests_mock):
    mock_responses = (
        ('GET', 'https://' + TEST_API_DOMAIN + '/v4/sell/fulfilment_points', 'mock_responses/ls_api/fulfilment_points.json', 200),
    )
    configure_mock_responses(requests_mock, mock_responses, FIXTURES_DIR, CONTENT_TYPE)

    resource_client = LiveStyledResourceClient(TEST_API_DOMAIN, 'bar')
    fps = list(resource_client.get_fulfilment_points())
    assert len(fps) == 30
    fps.sort(key=lambda o: o.id)
    fp = fps[0]
    assert isinstance(fp, FulfilmentPoint)
    assert fp.id == 1
    assert fp.status == 'ACTIVE'
    assert fp.reference == 'kartiks Collection point'
    assert fp.image_url == 'https://apiv3.s3.eu-west-1.amazonaws.com/fulfilmentpoint/German-Shepherd-Puppy-Fetch.jpg'
    assert fp.map_image_url == 'https://apiv3.s3.eu-west-1.amazonaws.com/fulfilmentpoint/british_summer_time_map_bigger.jpg'
    assert fp.lat == '38.026641'
    assert fp.lat == '38.026641'
    assert fp.type == 'VIRTUAL_QUEUE'
    assert fp.position == 0
    assert isinstance(fp.translations, list)
    assert isinstance(fp.translations[0], FulfilmentPointTranslation)
    assert fp.translations[0].language == 'en'
    assert fp.translations[0].title == 'Fulfilment point 1'
    assert fp.translations[0].description == 'Description'
    assert fp.translations[0].collection_note == 'Fulfillment note 1'
    assert isinstance(fp.categories, list)
    assert isinstance(fp.categories[0], FulfilmentPointCategory)
    assert isinstance(fp.audiences, list)
    assert isinstance(fp.audiences[0], Audience)
    assert isinstance(fp.audiences[1], Audience)
    assert fp.audiences[0].id == 1
    assert fp.audiences[1].id == 2
