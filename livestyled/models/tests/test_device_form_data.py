from livestyled.models.device_form_data import DeviceFormData
from livestyled.schemas.device_form_data import DeviceFormDataSchema


def test_create_device_form_data_from_deserialized():
    deserialized_data = {
        'id': 2,
        'device_id': 8,
        'form_id': 23,
        'data': [
            {
                'key': 'aaa',
                'value': 'test'
            }
        ],
        'created_at': '2020-05-19T10:05:15+00:00',
        'updated_at': '2020-05-19T10:05:15+00:00'
    }
    device_form_data = DeviceFormData(**deserialized_data)
    assert device_form_data


def test_serialize_device_form_data():
    deserialized_data = {
        'id': 2,
        'device_id': 8,
        'form_id': 23,
        'data': [
            {
                'key': 'aaa',
                'value': 'test'
            }
        ],
        'created_at': '2020-05-19T10:05:15+00:00',
        'updated_at': '2020-05-19T10:05:15+00:00'
    }
    device_form_data = DeviceFormData(**deserialized_data)
    serialized_form_data = DeviceFormDataSchema().dump(device_form_data)
    assert serialized_form_data
