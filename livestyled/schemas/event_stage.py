from marshmallow import EXCLUDE, fields, Schema

from livestyled.models.event_stage import EventStage
from livestyled.schemas.utils import get_id_from_url


class EventStageSchema(Schema):
    class Meta:
        unknown = EXCLUDE
        api_type = 'event_stages'
        url = 'v4/event_stages'
        model = EventStage

    id = fields.Int()
    status = fields.String()
    venue = fields.Function(get_id_from_url)
    name = fields.String()
    description = fields.String()
    color = fields.String()
    sort_id = fields.Int(data_key='sortId')
    updated_at = fields.AwareDateTime(data_key='updatedAt', allow_none=True)
    created_at = fields.AwareDateTime(data_key='createdAt', allow_none=True)
    app = fields.Function(get_id_from_url)
