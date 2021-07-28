from marshmallow import EXCLUDE, fields, Schema

from livestyled.models.fulfilment_point import (
    FulfilmentPoint,
    FulfilmentPointCategory,
    FulfilmentPointCategoryTranslation,
    FulfilmentPointTranslation,
)
from livestyled.schemas.audience import AudienceSchema
from livestyled.schemas.fields import RelatedResourceField, RelatedResourceLinkField
from livestyled.schemas.venue import VenueSchema


class FulfilmentPointTranslationSchema(Schema):
    class Meta:
        unknown = EXCLUDE
        model = FulfilmentPointTranslation

    language = fields.String()
    title = fields.String(missing=None)
    description = fields.String(missing=None)
    collection_note = fields.String(missing=None, data_key='collectionNote')


class FulfilmentPointCategoryTranslationSchema(Schema):
    class Meta:
        unknown = EXCLUDE
        model = FulfilmentPointCategoryTranslation

    id = fields.Int()
    language = fields.String()
    title = fields.String(missing=None)


class FulfilmentPointCategorySchema(Schema):
    class Meta:
        unknown = EXCLUDE
        model = FulfilmentPointCategory

    id = fields.Int()
    status = fields.String()
    translations = RelatedResourceField(schema=FulfilmentPointCategoryTranslationSchema, many=True)


class FulfilmentPointSchema(Schema):
    class Meta:
        unknown = EXCLUDE
        api_type = 'fulfilment_points'
        url = 'sell/fulfilment_points'
        model = FulfilmentPoint

    id = fields.Int()
    status = fields.String()
    image_url = fields.String(data_key='imageUrl', missing=None)
    map_image_url = fields.String(data_key='mapImageUrl', missing=None)
    lat = fields.String(missing=None)
    long = fields.String(missing=None)
    type = fields.String(missing=None)
    position = fields.Int(missing=None)
    reference = fields.String(missing=None)
    translations = fields.Nested(FulfilmentPointTranslationSchema, many=True)
    categories = RelatedResourceField(schema=FulfilmentPointCategorySchema, many=True, missing=[])
    venue = RelatedResourceLinkField(schema=VenueSchema, required=False, missing=None)
    external_id = fields.String(missing=None, data_key='externalId')
    audiences = fields.List(RelatedResourceLinkField(schema=AudienceSchema, microservice_aware=True), many=True, missing=[])
