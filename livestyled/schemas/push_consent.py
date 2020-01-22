from marshmallow import EXCLUDE, fields, Schema

from livestyled.schemas.utils import get_id_from_url


class PushConsentSchema(Schema):
    class Meta:
        unknown = EXCLUDE
        api_type = 'push_consents'
        url = 'v4/push_consents'

    id = fields.Int()
    type = fields.String()
    label = fields.String()
    title = fields.String()
    sort_id = fields.Int(data_key='sortId')
    updated_at = fields.AwareDateTime(data_key='updatedAt', allow_none=True)
    created_at = fields.AwareDateTime(data_key='createdAt', allow_none=True)
    app = fields.Function(get_id_from_url)
    translations = fields.Dict()  # TODO
