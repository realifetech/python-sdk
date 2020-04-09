from marshmallow import EXCLUDE, fields, Schema

from livestyled.models.booking import Booking


class BookingSchema(Schema):
    class Meta:
        unknown = EXCLUDE
        model = Booking
        api_type = 'bookings'
        url = 'v4/bookings'

    id = fields.Int()
    title = fields.String()
    device = fields.String()
    user = fields.String()
    event = fields.String()
    created_at = fields.String(data_key='createdAt')
    updated_at = fields.String(data_key='updatedAt')
    action = fields.String()
