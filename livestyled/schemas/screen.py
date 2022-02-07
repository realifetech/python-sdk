from marshmallow import EXCLUDE, fields, INCLUDE, Schema

from livestyled.models.screen import Screen, ScreenTranslation, ScreenVariation
from livestyled.schemas.fields import RelatedResourceLinkField


class ScreenTranslationSchema(Schema):
    class Meta:
        unknown = INCLUDE
        model = ScreenTranslation

    language = fields.String()
    title = fields.String()


class ScreenSchema(Schema):
    class Meta:
        unknown = EXCLUDE
        model = Screen
        api_type = 'screens'
        url = 'canvas/screens'

    id = fields.Int()
    reference = fields.String()
    screen_type = fields.String(data_key='screenType')
    translations = fields.List(fields.Nested(ScreenTranslationSchema))


class ScreenVariationSchema(Schema):
    class Meta:
        unknown = EXCLUDE
        api_type = 'screen_variation'
        url = 'canvas/screen_variations'
        model = ScreenVariation

    id = fields.Int()
    priority = fields.Int()
    created_at = fields.DateTime(data_key='createdAt', required=False, missing=None)
    updated_at = fields.DateTime(data_key='updatedAt', required=False, missing=None)
    screen = RelatedResourceLinkField(schema=ScreenSchema, allow_none=False, microservice_aware=True)
