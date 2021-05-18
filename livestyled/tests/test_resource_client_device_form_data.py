import os

from livestyled.models import Device, DeviceFormData
from livestyled.models.form import Form
from livestyled.resource_client import LiveStyledResourceClient
from livestyled.tests.utils import configure_mock_responses

FIXTURES_DIR = os.path.join(os.path.dirname(__file__), 'fixtures')
TEST_API_DOMAIN = 'test.livestyled.com'
CONTENT_TYPE = 'application/ld+json'


def test_get_form_data(requests_mock):
    mock_responses = (
        ('GET', 'https://' + TEST_API_DOMAIN + '/v4/engage/form_data', 'mock_responses/ls_api/engage/form_data.json', 200),
    )
    configure_mock_responses(requests_mock, mock_responses, FIXTURES_DIR, CONTENT_TYPE)

    resource_client = LiveStyledResourceClient(TEST_API_DOMAIN, 'bar')
    form_data = list(resource_client.get_form_data())
    assert len(form_data) == 30
    form_data.sort(key=lambda o: o.id)
    form_data_1 = form_data[0]
    assert isinstance(form_data_1, DeviceFormData)
    assert form_data_1.id == 1
    assert isinstance(form_data_1.data, list)
    assert isinstance(form_data_1.device, Device)
    assert isinstance(form_data_1.form, Form)
