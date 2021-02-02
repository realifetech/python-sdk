from marshmallow import EXCLUDE, fields, Schema

from livestyled.models.order import (
    Order,
    OrderItem,
)
from livestyled.schemas.app import AppSchema
from livestyled.schemas.fields import RelatedResourceField, RelatedResourceLinkField
from livestyled.schemas.fulfilment_point import FulfilmentPointSchema
from livestyled.schemas.product import ProductSchema, ProductVariantSchema
from livestyled.schemas.user import UserSchema


class OrderItemSchema(Schema):
    class Meta:
        unknown = EXCLUDE
        model = OrderItem

    id = fields.Int()
    product = RelatedResourceLinkField(schema=ProductSchema, missing=None)
    product_variant = RelatedResourceLinkField(schema=ProductVariantSchema, data_key='productVariant', missing=None, microservice_aware=True)
    fulfilment_point = RelatedResourceLinkField(schema=FulfilmentPointSchema, data_key='fulfilmentPoint', missing=None, microservice_aware=True)
    quantity = fields.Int()
    title = fields.String(missing=None)
    subtitle = fields.String(data_key='subtitle', missing=None)
    image_url = fields.String(data_key='imageUrl', missing=None)
    price = fields.Integer()
    total_price = fields.Integer(data_key='totalPrice')


class OrderSchema(Schema):
    class Meta:
        unknown = EXCLUDE
        api_type = 'orders'
        url = 'sell/orders'
        model = Order

    id = fields.Int()
    app = fields.Nested(AppSchema, missing=None)
    user = RelatedResourceLinkField(schema=UserSchema, missing=None, microservice_aware=True)
    status = fields.String(missing=None)
    gross_amount = fields.Integer(data_key='grossAmount', missing=None)
    discount = fields.Integer(missing=None)
    net_amount = fields.Integer(data_key='netAmount', missing=None)
    order_amount = fields.Integer(data_key='orderAmount', missing=None)
    order_number = fields.Integer(data_key='orderNumber', missing=None)
    items = RelatedResourceField(schema=OrderItemSchema, many=True, microservice_aware=True)
    external_id = fields.String(data_key='externalId', missing=None, allow_none=True)

    updated_at = fields.AwareDateTime(data_key='updatedAt', allow_none=True, missing=None)
    created_at = fields.AwareDateTime(data_key='createdAt', allow_none=True, missing=None)
    estimated_at = fields.AwareDateTime(data_key='estimated_at', allow_none=True, missing=None)
    collection_date = fields.Date(data_key='collectionDate', allow_none=True, missing=None)
    collection_preference_type = fields.String(data_key='collectionPreferenceType', allow_none=True, missing=None)
    check_in_time = fields.AwareDateTime(data_key='checkInTime', allow_none=True, missing=None)
    fulfilment_point = RelatedResourceLinkField(schema=FulfilmentPointSchema, data_key='fulfilmentPoint', missing=None, microservice_aware=True)
    seat_info = fields.Raw(data_key='seatInfo', missing=None, allow_none=True)
