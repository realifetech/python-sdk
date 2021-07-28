from marshmallow import EXCLUDE, fields, Schema

from livestyled.models.product import (
    Product,
    ProductCategory,
    ProductModifierItem,
    ProductModifierList,
    ProductVariant,
    ProductVariantStock
)
from livestyled.schemas.fields import RelatedResourceField, RelatedResourceLinkField
from livestyled.schemas.fulfilment_point import FulfilmentPointSchema


class ProductVariantStocksSchema(Schema):
    class Meta:
        unknown = EXCLUDE
        api_type = 'product_variant_stocks'
        url = 'sell/product_variant_stocks'

    id = fields.Integer()


class ProductVariantSchema(Schema):
    class Meta:
        unknown = EXCLUDE
        model = ProductVariant
        url = 'sell/product_variants'
        api_type = 'product_variants'

    class ProductVariantTranslationSchema(Schema):
        class Meta:
            unknown = EXCLUDE
        language = fields.String()
        title = fields.String()

    id = fields.Int()
    price = fields.Integer()
    stocks = RelatedResourceField(schema='livestyled.schemas.product.ProductVariantStockSchema', many=True,
                                  microservice_aware=True, missing=None)
    product = RelatedResourceLinkField(schema='livestyled.schemas.product.ProductSchema', microservice_aware=True)
    external_id = fields.String(missing=None, data_key='externalId')
    translations = fields.Nested(ProductVariantTranslationSchema, many=True, missing=None)
    tax = fields.String(missing=None)
    tax_rate = fields.String(missing=None, data_key='taxRate')
    tax_band = fields.String(missing=None, data_key='taxBand')


class ProductVariantStockSchema(Schema):
    class Meta:
        unknown = EXCLUDE
        model = ProductVariantStock
        api_type = 'product_variant_stocks'
        url = 'sell/product_variant_stocks'

    initial = fields.Integer()
    on_hand = fields.Integer(missing=None, data_key='onHand')
    fulfilment_point = RelatedResourceLinkField(schema=FulfilmentPointSchema, microservice_aware=True, data_key='fulfilmentPoint')
    product_variant = RelatedResourceLinkField(schema=ProductVariantSchema, microservice_aware=True, data_key='productVariant')


class ProductCategorySchema(Schema):
    class Meta:
        unknown = EXCLUDE
        model = ProductCategory
        api_type = 'product_categories'
        url = 'sell/product_categories'

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

    position = fields.Integer()
    image_url = fields.String(data_key='imageUrl', missing=None)
    external_id = fields.String(data_key='externalId', missing=None)


class ProductTranslationSchema(Schema):
    class Meta:
        unknown = EXCLUDE

    language = fields.String()
    title = fields.String(missing=None)
    description = fields.String(missing=None)


class CoreProductCategorySchema(Schema):
    class Meta:
        unknown = EXCLUDE
    id = fields.Integer()
    name = fields.String()


class ProductModifierItemTranslationsSchema(Schema):
    class Meta:
        unknown = EXCLUDE

    language = fields.String()
    title = fields.String(missing=None)


class ProductModifierItemSchema(Schema):
    class Meta:
        unknown = EXCLUDE
        model = ProductModifierItem
        url = 'sell/product_modifier_items'

    id = fields.Int()
    external_id = fields.String(data_key='externalId')
    status = fields.String(data_key='status')
    additional_price = fields.Integer(data_key='additionalPrice')
    translations = fields.Nested(ProductModifierItemTranslationsSchema, many=True, missing=[])
    modifier_list = RelatedResourceLinkField('livestyled.schemas.product.ProductModifierListSchema', data_key='modifierList', microservice_aware=True)
    status = fields.String(missing=None)


class ProductModifierListTranslationsSchema(Schema):
    class Meta:
        unknown = EXCLUDE

    language = fields.String()
    title = fields.String(missing=None)


class ProductModifierListSchema(Schema):
    class Meta:
        unknown = EXCLUDE
        model = ProductModifierList
        url = 'sell/product_modifier_lists'

    id = fields.Integer()
    status = fields.String()
    external_id = fields.String(data_key='externalId')
    reference = fields.String(missing=None)
    multiple_select = fields.Boolean(data_key='multipleSelect')
    mandatory_select = fields.Boolean(data_key='mandatorySelect')
    translations = fields.Nested(ProductModifierListTranslationsSchema, many=True, missing=[])
    items = RelatedResourceField(schema=ProductModifierItemSchema, many=True, missing=[], microservice_aware=True)


class ProductSchema(Schema):
    class Meta:
        unknown = EXCLUDE
        model = Product
        api_type = 'products'
        url = 'sell/products'

    id = fields.Int()
    status = fields.String(missing=None)
    reference = fields.String(missing=None)
    modifier_lists = fields.List(RelatedResourceLinkField(schema=ProductModifierListSchema, microservice_aware=True), data_key='modifierLists', many=True, missing=None)
    external_id = fields.String(data_key='externalId', missing=None)
    holding_time = fields.Raw(missing=None, data_key='holdingTime')
    reconciliation_group = fields.Raw(missing=None, data_key='reconciliation_group')
    images = fields.Nested(ProductImageSchema, many=True)
    categories = RelatedResourceField(schema=ProductCategorySchema, many=True, missing=[], microservice_aware=True)
    translations = fields.Nested(ProductTranslationSchema, many=True, missing=[])
    fulfilment_points = RelatedResourceField(schema=FulfilmentPointSchema, many=True, missing=[], data_key='fulfilmentPoints', microservice_aware=True)
    variants = RelatedResourceField(schema=ProductVariantSchema, many=True, missing=[], microservice_aware=True)
    core_product_category = fields.Nested(CoreProductCategorySchema, missing=None, data_key='coreProductCategory')
