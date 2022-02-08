import os

from livestyled.models import Widget, WidgetVariation
from livestyled.resource_client import LiveStyledResourceClient
from livestyled.tests.utils import configure_mock_responses


FIXTURES_DIR = os.path.join(os.path.dirname(__file__), 'fixtures')
TEST_API_DOMAIN = 'test.livestyled.com'
CONTENT_TYPE = 'application/ld+json'

REQUEST_BASE_URL = 'https://' + TEST_API_DOMAIN + '/v4/{}'


def test_get_widgets(requests_mock):
    mock_responses = (
        ('GET', REQUEST_BASE_URL.format('canvas/widgets'), 'mock_responses/ls_api/canvas/widgets.json', 200),
    )
    configure_mock_responses(requests_mock, mock_responses, FIXTURES_DIR, CONTENT_TYPE)

    resource_client = LiveStyledResourceClient(TEST_API_DOMAIN, 'bar')
    widgets = resource_client.get_widgets()
    assert isinstance(next(widgets), Widget)


def test_get_widget_item(requests_mock):
    item_endpoint = REQUEST_BASE_URL.format('canvas/widgets/1')
    mock_responses = (
        ('GET', item_endpoint, 'mock_responses/ls_api/canvas/item_widget.json', 200),
    )

    configure_mock_responses(requests_mock, mock_responses, FIXTURES_DIR, CONTENT_TYPE)

    resource_client = LiveStyledResourceClient(TEST_API_DOMAIN, 'bar')
    widget = resource_client.get_widget(id=1)
    assert isinstance(widget, Widget)


def test_get_widget_variations(requests_mock):
    item_endpoint = REQUEST_BASE_URL.format('canvas/widget_variations')
    mock_responses = (
        ('GET', item_endpoint, 'mock_responses/ls_api/canvas/widget_variations.json', 200),
        ('GET', REQUEST_BASE_URL.format('canvas/widgets/1'), 'mock_responses/ls_api/canvas/item_widget.json', 200),
    )

    configure_mock_responses(requests_mock, mock_responses, FIXTURES_DIR, CONTENT_TYPE)

    resource_client = LiveStyledResourceClient(TEST_API_DOMAIN, 'bar')
    widget_variations = resource_client.get_widget_variations()
    current_widget_variation = next(widget_variations)
    assert isinstance(current_widget_variation, WidgetVariation)
    assert isinstance(current_widget_variation.widget, Widget)
