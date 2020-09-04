from marshmallow import EXCLUDE, fields, Schema

from livestyled.models.product import (
    Product,
    ProductCategory,
    ProductImage,
    ProductModifierListTranslation,
    ProductTranslation,
    ProductVariant
)
from livestyled.schemas.fields import RelatedResourceField, RelatedResourceLinkField
from livestyled.schemas.fulfilment_point import FulfilmentPointSchema


class ProductVariantStocksSchema(Schema):
    class Meta:
        unknown = EXCLUDE

    id = fields.Integer()


class ProductVariantSchema(Schema):
    class Meta:
        unknown = EXCLUDE
        model = ProductVariant

    class ProductVariantTranslationSchema(Schema):
        class Meta:
            unknown = EXCLUDE
        language = fields.String()
        title = fields.String()

    id = fields.Int()
    price = fields.Integer()
    stocks = RelatedResourceLinkField(schema=ProductVariantStocksSchema, many=True, missing=[])
    product = RelatedResourceLinkField(schema='livestyled.schemas.product.ProductSchema')
    external_id = fields.String(missing=None, data_key='externalId')
    translations = fields.Nested(ProductVariantTranslationSchema, many=True, missing=None)


class ProductCategorySchema(Schema):
    class Meta:
        unknown = EXCLUDE
        model = ProductCategory
        api_type = 'product_categories'
        url = 'product_categories'

    class ProductCategoryTranslationSchema(Schema):
        class Meta:
            unknown = EXCLUDE
        language = fields.String()
        title = fields.String()

    id = fields.Int()
    reference = fields.String(missing=None)
    position = fields.Int()
    external_id = fields.String(missing=None, data_key='externalId')
    status = fields.String(missing=None)
    translations = fields.Nested(ProductCategoryTranslationSchema, many=True, missing=None)


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


class ProductModifierListTranslationsSchema(Schema):
    class Meta:
        unknown = EXCLUDE
        model = ProductModifierListTranslation

    id = fields.Int()
    language = fields.String()
    title = fields.String(missing=None)

    updated_at = fields.AwareDateTime(data_key='updatedAt', allow_none=True, missing=None)
    created_at = fields.AwareDateTime(data_key='createdAt', allow_none=True, missing=None)


class ProductModifierListsSchema(Schema):
    class Meta:
        unknown = EXCLUDE

    id = fields.Integer()
    status = fields.String()
    external_id = fields.String(data_key='externalId')
    multiple_select = fields.Boolean(data_key='multipleSelect')
    mandatory_select = fields.Boolean(data_key='mandatorySelect')
    translations = RelatedResourceField(schema=ProductModifierListTranslationsSchema, many=True, missing=[])


class ProductSchema(Schema):
    class Meta:
        unknown = EXCLUDE
        model = Product
        api_type = 'products'
        url = 'sell/products'

    id = fields.Int()
    status = fields.String(missing=None)
    reference = fields.String(missing=None)
    modifier_lists = RelatedResourceField(schema=ProductModifierListsSchema, many=True, missing=[], data_key='modifierLists')
    external_id = fields.String(data_key='externalId', missing=None)
    holding_time = fields.Raw(missing=None, data_key='holdingTime')
    reconciliation_group = fields.Raw(missing=None, data_key='reconciliation_group')
    images = RelatedResourceField(schema=ProductImageSchema, many=True)
    categories = RelatedResourceField(schema=ProductCategorySchema, many=True, missing=[])
    translations = RelatedResourceField(schema=ProductTranslationSchema, many=True, missing=[])
    fulfilment_points = RelatedResourceField(schema=FulfilmentPointSchema, many=True, missing=[], data_key='fulfilmentPoints')
    variants = RelatedResourceField(schema=ProductVariantSchema, many=True, missing=[])
    core_product_category = fields.Nested(CoreProductCategorySchema, missing=None, data_key='coreProductCategory')
