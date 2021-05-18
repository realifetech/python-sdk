from marshmallow import EXCLUDE, fields as field_package, Schema

from livestyled.models.form import Form


class FormSchema(Schema):
    class Meta:
        unknown = EXCLUDE
        model = Form
        api_type = 'form'
        url = 'engage/forms'
        default_ordering = 'id'

    id = field_package.Int()
    reference = field_package.String(data_key='reference', allow_none=True)
    image_url = field_package.String(data_key='imageUrl', allow_none=True)
    completion_button_url = field_package.String(data_key='completionButtonUrl', allow_none=True)
    completion_button_title = field_package.String(data_key='completionButtonTitle', allow_none=True)
    show_completion_date = field_package.Boolean(data_key='showCompletionDate', allow_none=True)
    allow_update = field_package.Boolean(data_key='allowUpdate', allow_none=True)
    refresh_on_success = field_package.Boolean(data_key='refreshOnSuccess', allow_none=True)
    requires_login = field_package.Boolean(data_key='requiresLogin', allow_none=True)
    fields = field_package.List(field_package.Inferred, data_key='fields', allow_none=True)
    translations = field_package.List(field_package.Inferred, data_key='translations', allow_none=True)
    validation_integration = field_package.String(data_key='validation_integration', allow_none=True)
