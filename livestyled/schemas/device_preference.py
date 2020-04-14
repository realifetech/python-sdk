from marshmallow import EXCLUDE, fields, Schema

from livestyled.models.device_preference import DevicePreference
from livestyled.schemas.device import DeviceSchema
from livestyled.schemas.event import EventSchema
from livestyled.schemas.fields import RelatedResourceLinkField
from livestyled.schemas.venue import VenueSchema


class DevicePreferenceSchema(Schema):
    class Meta:
        unknown = EXCLUDE
        model = DevicePreference
        api_type = 'device_preferences'
        url = 'v4/device_preferences'
        default_ordering = '-createdAt'

    id = fields.Int()
    created_at = fields.AwareDateTime(data_key='createdAt')
    venue_id = RelatedResourceLinkField(schema=VenueSchema, data_key='venue', allow_none=True)
    device_id = RelatedResourceLinkField(schema=DeviceSchema, data_key='device')
    event_id = RelatedResourceLinkField(schema=EventSchema, data_key='event', allow_none=True)
