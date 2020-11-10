from marshmallow import EXCLUDE, fields, Schema

from livestyled.models.reality import Reality, RealityType
from livestyled.schemas.fields import RelatedResourceLinkField


class RealityTypeSchema(Schema):
    class Meta:
        unknown = EXCLUDE
        api_type = 'reality_type'
        url = 'user_management/reality_types'
        model = RealityType

    id = fields.Int()
    name = fields.String(missing=None)
    config_json_schema = fields.Raw(missing={}, data_key='configJsonSchema', allow_none=True)
    config_ui_schema = fields.Raw(missing={}, data_key='configUiSchema', allow_none=True)
    evaluator = fields.Raw(missing={})
    watch = fields.Raw()
    value_type = fields.String(data_key='valueType')
    updated_at = fields.AwareDateTime(data_key='updatedAt', allow_none=True, missing=None)
    created_at = fields.AwareDateTime(data_key='createdAt', allow_none=True, missing=None)
    combination_key = fields.String(data_key='combinationKey', allow_none=True, missing=None)


class RealitySchema(Schema):
    class Meta:
        unknown = EXCLUDE
        api_type = 'realities'
        url = 'user_management/realities'
        model = Reality

    id = fields.Int()
    reality_type = RelatedResourceLinkField(schema=RealityTypeSchema, allow_none=False, data_key='realityType', microservice_aware=True)
    name = fields.String(missing=None)
    config = fields.Raw(missing={})
    updated_at = fields.AwareDateTime(data_key='updatedAt', allow_none=True, missing=None)
    created_at = fields.AwareDateTime(data_key='createdAt', allow_none=True, missing=None)
    status = fields.String()
