from marshmallow import EXCLUDE, fields, Schema

from livestyled.models.audience import Audience
from livestyled.schemas.fields import RelatedResourceLinkField
from livestyled.schemas.reality import RealitySchema


class AudienceRealityValuesValueSchema(Schema):
    operator = fields.String()
    value = fields.String()


class AudienceRealityValuesSchema(Schema):
    reality = RelatedResourceLinkField(schema=RealitySchema, microservice_aware=True)
    values = fields.Nested(AudienceRealityValuesValueSchema, many=True)


class AudienceSchema(Schema):
    class Meta:
        unknown = EXCLUDE
        api_type = 'audiences'
        url = 'user_management/audiences'
        model = Audience

    id = fields.Int()
    name = fields.String(missing=None)
    reality_values = fields.Nested(AudienceRealityValuesSchema, many=True, data_key='realityValues')
    updated_at = fields.AwareDateTime(data_key='updatedAt', allow_none=True, missing=None)
    created_at = fields.AwareDateTime(data_key='createdAt', allow_none=True, missing=None)
