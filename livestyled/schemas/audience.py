from typing import List

from marshmallow import EXCLUDE, fields, pre_load, Schema

from livestyled.models.audience import Audience
from livestyled.schemas.fields import RelatedResourceLinkField
from livestyled.schemas.reality import RealitySchema


class AudienceRealityValuesValueSchema(Schema):
    operator = fields.String()
    value = fields.Raw()

    @pre_load
    def pre_process_value(self, data, **kwarg):
        if isinstance(data['value'], List):
            data['value'] = [(lambda x: str(x))(x) for x in data['value']]
        else:
            data['value'] = str(data['value'])
        return data


class AudienceRealityValuesSchema(Schema):
    reality = RelatedResourceLinkField(schema=RealitySchema, microservice_aware=True)
    values = fields.Nested(AudienceRealityValuesValueSchema, many=True)
    condition = fields.String(missing=None)


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
