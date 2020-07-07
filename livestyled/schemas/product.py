from marshmallow import EXCLUDE, fields, Schema

from livestyled.models.product import (
    Product,
    ProductCategory,
    ProductImage,
    ProductTranslation,
    ProductVariant
)
from livestyled.schemas.fields import RelatedResourceField, RelatedResourceLinkField
from livestyled.schemas.fulfilment_point import FulfilmentPointSchema


class ProductVariantSchema(Schema):
    class Meta:
        unknown = EXCLUDE
        model = ProductVariant

    id = fields.Int()
    price = fields.Integer()
    stocks = fields.List(fields.String)


class ProductCategorySchema(Schema):
    class Meta:
        unknown = EXCLUDE
        model = ProductCategory
        api_type = 'product_categories'
        url = 'v4/product_categories'

    id = fields.Int()
    reference = fields.String(missing=None)
    position = fields.Int()


class ProductImageSchema(Schema):
    class Meta:
        unknown = EXCLUDE
        model = ProductImage

    id = fields.Integer()
    product = RelatedResourceLinkField(schema='livestyled.schemas.order.ProductSchema')
    position = fields.Integer()
    image_url = fields.String(data_key='imageUrl', missing=None)
    external_id = fields.String(data_key='externalId', missing=None)

    updated_at = fields.AwareDateTime(data_key='updatedAt', allow_none=True, missing=None)
    created_at = fields.AwareDateTime(data_key='createdAt', allow_none=True, missing=None)


class ProductTranslationSchema(Schema):
    class Meta:
        unknown = EXCLUDE
        model = ProductTranslation

    id = fields.Int()
    language = fields.String()
    title = fields.String(missing=None)
    description = fields.String(missing=None)

    updated_at = fields.AwareDateTime(data_key='updatedAt', allow_none=True, missing=None)
    created_at = fields.AwareDateTime(data_key='createdAt', allow_none=True, missing=None)


class CoreProductCategorySchema(Schema):
    class Meta:
        unknown = EXCLUDE
    id = fields.Integer()
    name = fields.String()


class ProductSchema(Schema):
    class Meta:
        unknown = EXCLUDE
        model = Product
        api_type = 'products'
        url = 'v4/products'

    id = fields.Int()
    status = fields.String(missing=None)
    reference = fields.String(missing=None)
    modifier_lists = fields.Raw(missing=[], data_key='modifierLists')
    external_id = fields.String(data_key='externalId', missing=None)
    holding_time = fields.Raw(missing=None, data_key='holdingTime')
    reconciliation_group = fields.Raw(missing=None, data_key='reconciliation_group')
    images = RelatedResourceField(schema=ProductImageSchema, many=True)
    categories = RelatedResourceField(schema=ProductCategorySchema, many=True, missing=[])
    translations = RelatedResourceField(schema=ProductTranslationSchema, many=True, missing=[])
    fulfilment_points = RelatedResourceLinkField(schema=FulfilmentPointSchema, many=True, missing=[], data_key='fulfilmentPoints')
    variants = RelatedResourceLinkField(schema=ProductVariantSchema, many=True, missing=[])
    core_product_category = fields.Nested(CoreProductCategorySchema, missing=None, data_key='coreProductCategory')
