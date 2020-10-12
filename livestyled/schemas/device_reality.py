from marshmallow import EXCLUDE, fields, Schema

from livestyled.models.device_reality import DeviceReality
from livestyled.schemas.device import DeviceSchema
from livestyled.schemas.fields import RelatedResourceLinkField
from livestyled.schemas.reality import RealitySchema


class DeviceRealitySchema(Schema):
    class Meta:
        unknown = EXCLUDE
        api_type = 'device_realities'
        url = 'user_management/device_realities'
        model = DeviceReality

    id = fields.Int()
    reality = RelatedResourceLinkField(schema=RealitySchema, allow_none=False)
    device = RelatedResourceLinkField(schema=DeviceSchema, allow_none=False)
    value = fields.String(missing=None)
    updated_at = fields.AwareDateTime(data_key='updatedAt', allow_none=True, missing=None)
    created_at = fields.AwareDateTime(data_key='createdAt', allow_none=True, missing=None)
