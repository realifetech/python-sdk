from marshmallow import EXCLUDE, fields, Schema

from livestyled.models.push_broadcast import PushBroadcast
from livestyled.schemas.fields import RelatedResourceLinkField
from livestyled.schemas.push_consent import PushConsentSchema


class PushBroadcastSchema(Schema):
    class Meta:
        unknown = EXCLUDE
        api_type = 'push_broadcasts'
        url = 'v4/push_broadcasts'
        publish_url = 'v4/push_broadcasts/publish'
        model = PushBroadcast

    id = fields.Int(required=False, allow_none=False)
    title = fields.String(data_key='title')
    message = fields.String(data_key='message')
    deep_link = fields.String(data_key='deepLink')
    ttl = fields.Int()
    message_id = fields.String(data_key='messageId')
    delivered = fields.Int()
    updated_at = fields.AwareDateTime(data_key='updatedAt', allow_none=True)
    created_at = fields.AwareDateTime(data_key='createdAt', allow_none=True)
    push_consent_id = RelatedResourceLinkField(schema=PushConsentSchema, data_key='pushConsent')
