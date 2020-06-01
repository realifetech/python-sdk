from marshmallow import EXCLUDE, fields, Schema

from livestyled.models.event import Event
from livestyled.schemas.utils import get_id_from_url


class EventIntegrationSchema(Schema):
    class Meta:
        unknown = EXCLUDE
        api_type = 'event_integration'
        url = 'v4/event_integration'
        model = Event

    id = fields.Int()
    status = fields.String()
    endpoint_url = fields.Url(data_key='endpointUrl')
    timezone = fields.String()
    adapter = fields.String()
    config_payload = fields.String(data_key='configPayload')
    updated_at = fields.AwareDateTime(data_key='updatedAt', allow_none=True)
    created_at = fields.AwareDateTime(data_key='createdAt', allow_none=True)
    app = fields.Function(get_id_from_url)
    remove_old = fields.Boolean(data_key='removeOld')
    override_social_media = fields.Boolean(data_key='overrideSocialMedia')
