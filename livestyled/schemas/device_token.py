from marshmallow import EXCLUDE, fields, Schema

from livestyled.models import DeviceToken
from livestyled.schemas.device import DeviceSchema
from livestyled.schemas.fields import RelatedResourceLinkField


class DeviceTokenSchema(Schema):
    class Meta:
        unknown = EXCLUDE
        api_type = 'device_tokens'
        url = 'v4/device_tokens'
        model = DeviceToken

    id = fields.Int()
    provider = fields.String()
    provider_token = fields.String(data_key='providerToken')
    payload = fields.Raw(allow_none=True)
    device_id = RelatedResourceLinkField(schema=DeviceSchema, data_key='device')
