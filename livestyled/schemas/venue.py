from marshmallow import EXCLUDE, fields, Schema

from livestyled.schemas.utils import get_id_from_url


class VenueSchema(Schema):
    class Meta:
        unknown = EXCLUDE
        api_type = 'venues'
        url = 'v4/venues'

    id = fields.Int()
    label = fields.String()
    name = fields.String()
    status = fields.String()
    is_default = fields.Boolean(data_key='is_default')
    useful_info = fields.List(fields.Inferred, data_key='usefulInfo')  # TODO
    event_useful_info = fields.List(fields.Inferred, data_key='eventUsefulInfo')  # TODO
    app = fields.Function(get_id_from_url)
    social_media = fields.List(fields.Inferred, data_key='socialMedia')  # TODO
