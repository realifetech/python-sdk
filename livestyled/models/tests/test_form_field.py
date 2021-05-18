from livestyled.models.form_field import FormField
from livestyled.schemas.form_field import FormFieldSchema


def test_create_form_field_from_deserialized():
    deserialized_data = {
        'id': 47,
        'type': 'radio',
        'key': 'radio',
        'validation_regex': 'Test',
        'required': True,
        'select_options': [
            {
                'id': 19,
                'title': 'YES',
                'value': 'YES',
                'icon_url': 'https://cdn3.iconfinder.com/data/icons/flat-actions-icons-9/792/Tick_Mark_Dark-512.png'
            },
            {
                'id': 20,
                'title': 'NO',
                'value': 'NO',
                'icon_url': 'https://lh3.googleusercontent.com/proxy/fN1ayBfVrzPB8xZiqM5k38g6FkdY4EuSR3QuT2EBqwjyH7L8RqEXm4hc34k8E6FAdD5mbmHje0n_hIl6l5saUXH26Ak5b-gWo2iKBPbYTQ9HHlti'
            }
        ],
        'translations': [
            {
                'id': 12,
                'language': 'en',
                'label': 'RadioButton Label',
                'placeholder': 'RadioButton Placeholder 2',
                'validation_error': 'RadioButtonError2'
            }
        ],
        'sort_id': 2,
        'auto_fill': None
    }
    form_field = FormField(**deserialized_data)
    assert form_field


def test_serialize_form_field():
    deserialized_data = {
        'id': 47,
        'type': 'radio',
        'key': 'radio',
        'validation_regex': 'Test',
        'required': True,
        'select_options': [
            {
                'id': 19,
                'title': 'YES',
                'value': 'YES',
                'icon_url': 'https://cdn3.iconfinder.com/data/icons/flat-actions-icons-9/792/Tick_Mark_Dark-512.png'
            },
            {
                'id': 20,
                'title': 'NO',
                'value': 'NO',
                'icon_url': 'https://lh3.googleusercontent.com/proxy/fN1ayBfVrzPB8xZiqM5k38g6FkdY4EuSR3QuT2EBqwjyH7L8RqEXm4hc34k8E6FAdD5mbmHje0n_hIl6l5saUXH26Ak5b-gWo2iKBPbYTQ9HHlti'
            }
        ],
        'translations': [
            {
                'id': 12,
                'language': 'en',
                'label': 'RadioButton Label',
                'placeholder': 'RadioButton Placeholder 2',
                'validation_error': 'RadioButtonError2'
            }
        ],
        'sort_id': 2,
        'auto_fill': None
    }
    form_field = FormField(**deserialized_data)
    serialized_form_field = FormFieldSchema().dump(form_field)
    assert serialized_form_field
