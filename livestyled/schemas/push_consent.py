from marshmallow import EXCLUDE, fields, Schema

from livestyled.models.push_consent import PushConsent


class PushConsentSchema(Schema):
    class Meta:
        unknown = EXCLUDE
        api_type = 'push_consents'
        url = 'v4/push_consents'
        model = PushConsent

    id = fields.Int()
    type = fields.String()
    label = fields.String()
    title = fields.String()
    sort_id = fields.Int(data_key='sortId')
    updated_at = fields.AwareDateTime(data_key='updatedAt', allow_none=True)
    created_at = fields.AwareDateTime(data_key='createdAt', allow_none=True)
    translations = fields.Raw()
