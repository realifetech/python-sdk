from marshmallow import EXCLUDE, fields, Schema

from livestyled.schemas.utils import get_id_from_url


class EventSchema(Schema):
    class Meta:
        unknown = EXCLUDE
        api_type = 'events'
        url = 'v4/events'

    id = fields.Int()
    status = fields.String()
    type = fields.String()
    title = fields.String()
    description = fields.String()
    image_url = fields.Url(data_key='image_url')
    promoted = fields.Boolean()
    updated_at = fields.AwareDateTime(data_key='updatedAt', allow_none=True)
    event_dates = fields.List(fields.Dict, data_key='eventDates')  # TODO
    app = fields.Function(get_id_from_url)
    venues = fields.List(fields.Inferred),  # TODO
    artists = fields.List(fields.Inferred),  # TODO
    useful_info = fields.List(fields.Inferred, data_key='usefulInfo'),  # TODO
    user_actions = fields.List(fields.Inferred, data_key='userActions'),  # TODO
    social_media = fields.List(fields.Inferred, data_key='socialMedia'),  # TODO
    translations = fields.List(fields.Inferred),  # TODO
