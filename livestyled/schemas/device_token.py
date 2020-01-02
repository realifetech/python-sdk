from marshmallow import EXCLUDE, fields, Schema

from livestyled.schemas.utils import get_id_from_url


class DeviceTokenSchema(Schema):
    class Meta:
        unknown = EXCLUDE

    id = fields.Int()
    provider = fields.String()
    provider_token = fields.String(data_key='providerToken')
    payload = fields.Dict(keys=fields.String(), allow_none=True)
    device = fields.Function(deserialize=get_id_from_url)
