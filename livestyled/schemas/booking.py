from marshmallow import EXCLUDE, fields, Schema

from livestyled.models.booking import Booking
from livestyled.schemas.device import DeviceSchema
from livestyled.schemas.event import EventSchema
from livestyled.schemas.fields import RelatedResourceLinkField
from livestyled.schemas.user import UserSchema


class BookingSchema(Schema):
    class Meta:
        unknown = EXCLUDE
        model = Booking
        api_type = 'bookings'
        url = 'v4/bookings'

    id = fields.Int()
    title = fields.String()
    device_id = RelatedResourceLinkField(schema=DeviceSchema, data_key='device')
    user_id = RelatedResourceLinkField(schema=UserSchema, data_key='user')
    event_id = RelatedResourceLinkField(schema=EventSchema, data_key='event')
    created_at = fields.String(data_key='createdAt')
    updated_at = fields.String(data_key='updatedAt')
    action = fields.String()
