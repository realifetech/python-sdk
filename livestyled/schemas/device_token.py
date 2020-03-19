from marshmallow import EXCLUDE, fields, Schema

from livestyled.schemas.utils import get_id_from_url


class DeviceTokenSchema(Schema):
    class Meta:
        unknown = EXCLUDE
        api_type = 'device_tokens'
        url = 'v4/device_tokens'

    id = fields.Int()
    provider = fields.String()
    provider_token = fields.String(data_key='providerToken')
    payload = fields.Raw(allow_none=True)
    device = fields.Function(deserialize=get_id_from_url)
