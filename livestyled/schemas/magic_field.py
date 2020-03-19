from marshmallow import EXCLUDE, fields, Schema

from livestyled.models.magic_field import MagicField
from livestyled.schemas.fields import RelatedResourceLinkField


class MagicFieldSchema(Schema):
    class Meta:
        unknown = EXCLUDE
        api_type = 'magic_fields'
        url = 'v4/magic_fields'
        model = MagicField

    id = fields.Int()
    key = fields.String()
    value = fields.String()
    user_id = RelatedResourceLinkField(schema='livestyled.schemas.user.UserSchema', required=False, missing=None, data_key='user')
