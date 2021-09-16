from marshmallow import EXCLUDE, fields, Schema

from livestyled.models.payment import MerchantAccount, PaymentCustomer, PaymentGateway, PaymentSource
from livestyled.schemas.fields import RelatedResourceField, RelatedResourceLinkField
from livestyled.schemas.fulfilment_point import FulfilmentPointSchema
from livestyled.schemas.user import UserSchema


class PaymentCustomerSchema(Schema):
    class Meta:
        unknown = EXCLUDE
        api_type = 'payment_customers'
        url = 'payment/payment_customers'
        model = PaymentCustomer

    id = fields.Int(missing=None)
    user_id = RelatedResourceLinkField(schema=UserSchema, data_key='user', microservice_aware=True)
    external_ids = fields.Dict()
    payment_sources = fields.List(fields.Dict())


class PaymentGatewaySchema(Schema):
    class Meta:
        unknown = EXCLUDE
        api_type = 'payment_gateways'
        url = 'payment/payment_gateways'
        model = PaymentGateway

    id = fields.Int(missing=None)
    config_ui_schema = fields.Dict(data_key='configUiSchema', allow_none=True)
    payment_gateway = fields.String(data_key='paymentGateway')
    name = fields.String()


class PaymentSourceSchema(Schema):
    class Meta:
        unknown = EXCLUDE
        api_type = 'payment_sources'
        url = 'payment/payment_sources'
        model = PaymentSource

    id = fields.Int(missing=None)
    status = fields.String()
    payment_customer_id = RelatedResourceLinkField(schema=PaymentCustomerSchema, data_key='paymentCustomer', microservice_aware=True)
    token_provider = fields.String()
    external_id = fields.String()
    psp = fields.String()
    type = fields.String()
    default = fields.Bool()
    billing_details = fields.Dict(data_key='billingDetails')
    card = fields.Dict()
    psp_tokens: fields.List(fields.Dict())


class MerchantAccountSchema(Schema):
    class Meta:
        unknown = EXCLUDE
        api_type = 'merchant_accounts'
        url = 'payment/merchant_accounts'
        model = MerchantAccount

    id = fields.Int(missing=None)
    status = fields.String()
    payment_gateway_id = RelatedResourceLinkField(schema=PaymentGatewaySchema, data_key='paymentGateway', microservice_aware=True)
    config = fields.Dict(allow_none=True)
    label = fields.String()
    fulfilment_points = RelatedResourceField(schema=FulfilmentPointSchema, many=True, data_key='fulfilmentPoints')
