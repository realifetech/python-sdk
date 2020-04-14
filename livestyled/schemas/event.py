from marshmallow import EXCLUDE, fields, Schema

from livestyled.models import Event
from livestyled.schemas.utils import get_id_from_url


class EventDate(Schema):
    class Meta:
        unknown = EXCLUDE

    id = fields.Int()
    start_at = fields.AwareDateTime(data_key='startAt')
    end_at = fields.AwareDateTime(data_key='endAt')
    general_ticket_url = fields.String(data_key='generalTicketUrl', required=False)


class EventSchema(Schema):
    class Meta:
        unknown = EXCLUDE
        api_type = 'events'
        url = 'v4/events'
        model = Event

    id = fields.Int()
    status = fields.String()
    type = fields.String()
    title = fields.String()
    description = fields.String()
    image_url = fields.Url(data_key='imageUrl')
    promoted = fields.Boolean()
    event_dates = fields.Nested(EventDate, data_key='eventDates', many=True)
    app = fields.Function(get_id_from_url)
    venues = fields.List(fields.Inferred),  # TODO
    artists = fields.List(fields.Inferred),  # TODO
    useful_info = fields.List(fields.Inferred, data_key='usefulInfo'),  # TODO
    user_actions = fields.List(fields.Inferred, data_key='userActions'),  # TODO
    social_media = fields.List(fields.Inferred, data_key='socialMedia'),  # TODO
    translations = fields.List(fields.Inferred),  # TODO
    updated_at = fields.AwareDateTime(data_key='updatedAt', allow_none=True)
    created_at = fields.AwareDateTime(data_key='createdAt', allow_none=True)
