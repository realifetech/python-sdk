from marshmallow import EXCLUDE, fields, Schema

from livestyled.models.payment import MerchantAccount, PaymentCustomer, PaymentGateway, PaymentIntent, PaymentSource
from livestyled.schemas.fields import RelatedResourceField, RelatedResourceLinkField
from livestyled.schemas.fulfilment_point import FulfilmentPointSchema
from livestyled.schemas.order import OrderSchema
from livestyled.schemas.user import UserSchema


class PaymentCustomerSchema(Schema):
    class Meta:
        unknown = EXCLUDE
        api_type = 'payment_customers'
        url = 'payment/payment_customers'
        model = PaymentCustomer

    id = fields.Int(missing=None)
    user_id = RelatedResourceLinkField(schema=UserSchema, data_key='user', microservice_aware=True)
    external_ids = fields.Dict(data_key='externalIds')
    payment_sources = fields.List(fields.Dict(), data_key='paymentSources')


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
    token_provider = fields.String(data_key='tokenProvider')
    external_id = fields.String(data_key='externalId')
    psp = fields.String()
    type = fields.String()
    default = fields.Bool()
    billing_details = fields.Dict(data_key='billingDetails')
    card = fields.Dict()
    psp_tokens: fields.List(fields.Dict())


class PaymentIntentSchema(Schema):
    class Meta:
        unknown = EXCLUDE
        api_type = 'payment_intents'
        url = 'payment/payment_intents'
        model = PaymentIntent

    id = fields.Int(missing=None)
    external_id = fields.String(data_key='externalId', missing=None)
    payment_customer_id = RelatedResourceLinkField(schema=PaymentCustomerSchema, data_key='paymentCustomer', microservice_aware=True)
    status = fields.String()
    amount = fields.Int()
    currency = fields.String()
    last_payment_error = fields.String(data_key='lastPaymentError')
    live_mode = fields.Bool(data_key='liveMode')
    save_payment_source = fields.Bool(data_key='savePaymentSource')
    next_action = fields.Dict(data_key='nextAction')
    order_type = fields.String(data_key='orderType')
    order = RelatedResourceLinkField(schema=OrderSchema, data_key='orderId', microservice_aware=True)


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
