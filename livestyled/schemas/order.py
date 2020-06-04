from marshmallow import EXCLUDE, fields, Schema

from livestyled.models.order import (
    Order,
    OrderItem,
)
from livestyled.schemas.fields import RelatedResourceField
from livestyled.schemas.fulfilment_point import FulfilmentPointSchema
from livestyled.schemas.product import ProductSchema, ProductVariantSchema
from livestyled.schemas.user import UserSchema


class OrderItemSchema(Schema):
    class Meta:
        unknown = EXCLUDE
        model = OrderItem

    id = fields.Int()
    product = RelatedResourceField(schema=ProductSchema, missing=None)
    product_variant = RelatedResourceField(schema=ProductVariantSchema, data_key='productVariant')
    fulfilment_point = RelatedResourceField(schema=FulfilmentPointSchema, data_key='fulfilmentPoint')
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
        url = 'v4/orders'
        model = Order

    id = fields.Int()
    user = fields.Nested(UserSchema, missing=None)
    status = fields.String(missing=None)
    gross_amount = fields.Integer(data_key='grossAmount', missing=None)
    discount = fields.Integer(missing=None)
    net_amount = fields.Integer(data_key='netAmount', missing=None)
    order_amount = fields.Integer(data_key='orderAmount', missing=None)
    order_number = fields.Integer(data_key='orderNumber', missing=None)
    items = RelatedResourceField(schema=OrderItemSchema, many=True)

    updated_at = fields.AwareDateTime(data_key='updatedAt', allow_none=True, missing=None)
    created_at = fields.AwareDateTime(data_key='createdAt', allow_none=True, missing=None)
