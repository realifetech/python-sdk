from livestyled.models.form import Form
from livestyled.schemas.form import FormSchema


def test_create_form_from_deserialized():
    deserialized_data = {
        'id': 24,
        'reference': 'Waiver Form IMS',
        'image_url': 'https://apiv3-dev.s3.eu-west-1.amazonaws.com/form/20200201_110848-PANO.jpg',
        'completion_button_url': 'https://www.google.com',
        'completion_button_title': 'Complete NOT THIS ONE',
        'show_completion_date': True,
        'allow_update': True,
        'refresh_on_success': True,
        'validation_integration': '/integration/integrations/5',
        'fields': [
            {
                'id': 100,
                'type': 'text',
                'key': 'code',
                'required': True,
                'select_options': [],
                'translations': [
                    {
                        'id': 60,
                        'language': 'en',
                        'label': 'code',
                        'placeholder': 'code',
                        'validation_error': 'code'
                    }
                ],
                'sort_id': 1
            }
        ],
        'translations': [
            {
                'id': 17,
                'language': 'en',
                'title': 'Waiver Form IMS',
                'description': 'Waiver Form IMS',
                'submit_button_title': 'Submit',
                'completion_button_title': 'HERE AMY',
                'completion_title': 'Thanks parcero',
                'completion_description': 'Thanks parcero'
            }
        ],
        'requires_login': True
    }
    form = Form(**deserialized_data)
    assert form


def test_serialize_form():
    deserialized_data = {
        'id': 24,
        'reference': 'Waiver Form IMS',
        'image_url': 'https://apiv3-dev.s3.eu-west-1.amazonaws.com/form/20200201_110848-PANO.jpg',
        'completion_button_url': 'https://www.google.com',
        'completion_button_title': 'Complete NOT THIS ONE',
        'show_completion_date': True,
        'allow_update': True,
        'refresh_on_success': True,
        'validation_integration': '/integration/integrations/5',
        'fields': [
            {
                'id': 100,
                'type': 'text',
                'key': 'code',
                'required': True,
                'select_options': [],
                'translations': [
                    {
                        'id': 60,
                        'language': 'en',
                        'label': 'code',
                        'placeholder': 'code',
                        'validation_error': 'code'
                    }
                ],
                'sort_id': 1
            }
        ],
        'translations': [
            {
                'id': 17,
                'language': 'en',
                'title': 'Waiver Form IMS',
                'description': 'Waiver Form IMS',
                'submit_button_title': 'Submit',
                'completion_button_title': 'HERE AMY',
                'completion_title': 'Thanks parcero',
                'completion_description': 'Thanks parcero'
            }
        ],
        'requires_login': True
    }
    form = Form(**deserialized_data)
    serialized_form = FormSchema().dump(form)
    assert serialized_form
