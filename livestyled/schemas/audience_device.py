from marshmallow import EXCLUDE, fields, Schema

from livestyled.models.audience_device import AudienceDevice
from livestyled.schemas.fields import RelatedResourceLinkField
from livestyled.schemas.audience import AudienceSchema
from livestyled.schemas.device import DeviceSchema


class AudienceDeviceSchema(Schema):
    class Meta:
        unknown = EXCLUDE
        api_type = 'audience_devices'
        url = 'user_management/audience_devices'
        model = AudienceDevice

    audience = RelatedResourceLinkField(schema=AudienceSchema)
    device = RelatedResourceLinkField(schema=DeviceSchema)
    created_at = fields.AwareDateTime(data_key='createdAt', allow_none=True, missing=None)
