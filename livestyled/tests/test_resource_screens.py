import os
import time

from livestyled.models import Screen, Widget, WidgetVariation
from livestyled.resource_client import LiveStyledResourceClient
from livestyled.tests.utils import configure_mock_responses


FIXTURES_DIR = os.path.join(os.path.dirname(__file__), 'fixtures')
TEST_API_DOMAIN = 'test.livestyled.com'
CONTENT_TYPE = 'application/ld+json'

REQUEST_BASE_URL = 'https://' + TEST_API_DOMAIN + '/v4/{}'


def test_get_screens(requests_mock):
    mock_responses = (
        ('GET', REQUEST_BASE_URL.format('canvas/screens'), 'mock_responses/ls_api/canvas/screens.json', 200),
    )
    configure_mock_responses(requests_mock, mock_responses, FIXTURES_DIR, CONTENT_TYPE)

    resource_client = LiveStyledResourceClient(TEST_API_DOMAIN, 'bar')
    screens = resource_client.get_screens()
    assert isinstance(next(screens), Screen)


def test_get_screens_widget_by_audience(requests_mock):
    collection_endpoint = REQUEST_BASE_URL.format('canvas/screens/1/widgets_by_audience?audience=1')
    mock_responses = (
        ('GET', collection_endpoint, 'mock_responses/ls_api/canvas/widgets_by_audience.json', 200),
    )

    configure_mock_responses(requests_mock, mock_responses, FIXTURES_DIR, CONTENT_TYPE)

    resource_client = LiveStyledResourceClient(TEST_API_DOMAIN, 'bar')
    widgets = resource_client.get_widgets_by_audience(screen_id=1, audience_id=1, timestamp=time.time())
    current_widget = next(widgets)
    assert isinstance(current_widget, Widget)
    assert isinstance(current_widget.variation, WidgetVariation)


def test_get_screens_item(requests_mock):
    item_endpoint = REQUEST_BASE_URL.format('canvas/screens/1')
    mock_responses = (
        ('GET', item_endpoint, 'mock_responses/ls_api/canvas/item_screen.json', 200),
    )

    configure_mock_responses(requests_mock, mock_responses, FIXTURES_DIR, CONTENT_TYPE)

    resource_client = LiveStyledResourceClient(TEST_API_DOMAIN, 'bar')
    widget = resource_client.get_screen(id=1)
    assert isinstance(widget, Screen)
