from marshmallow import EXCLUDE, fields, Schema

from livestyled.models.device_form_data import DeviceFormData
from livestyled.schemas.device import DeviceSchema
from livestyled.schemas.fields import RelatedResourceLinkField
from livestyled.schemas.form import FormSchema


class DeviceFormDataSchema(Schema):
    class Meta:
        unknown = EXCLUDE
        model = DeviceFormData
        api_type = 'form_data'
        url = 'engage/form_data'
        default_ordering = 'id'

    id = fields.Int()
    expires_at = fields.AwareDateTime(data_key='expiresAt', load_only=True, allow_none=True)
    created_at = fields.AwareDateTime(data_key='createdAt', load_only=True, allow_none=True)
    updated_at = fields.AwareDateTime(data_key='updatedAt', load_only=True, allow_none=True)
    data = fields.List(fields.Inferred, data_key='data')
    device_id = RelatedResourceLinkField(schema=DeviceSchema, data_key='device', microservice_aware=True)
    form_id = RelatedResourceLinkField(schema=FormSchema, data_key='form', microservice_aware=True)
