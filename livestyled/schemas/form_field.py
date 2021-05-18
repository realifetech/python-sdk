from marshmallow import EXCLUDE, fields, Schema

from livestyled.models.form_field import FormField


class FormFieldSchema(Schema):
    class Meta:
        unknown = EXCLUDE
        model = FormField
        api_type = 'form_field'
        url = 'form_fields'
        default_ordering = 'id'

    id = fields.Int()
    type = fields.String(data_key='type', allow_none=True)
    key = fields.String(data_key='key', allow_none=True)
    validation_regex = fields.String(data_key='validationRegex', allow_none=True)
    required = fields.Boolean(data_key='required', allow_none=True, default=False)
    select_options = fields.List(fields.Inferred, data_key='selectOptions', allow_none=True)
    sort_id = fields.Int(data_key='sortId', allow_none=True)
    translations = fields.List(fields.Inferred, data_key='translations', allow_none=True)
    auto_fill = fields.Dict(data_key='auto_fill', allow_none=True)
