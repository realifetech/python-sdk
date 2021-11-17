from marshmallow import EXCLUDE, fields, Schema

from livestyled.models.payment import (
    MerchantAccount, MerchantAccountFulfilmentPoint, MerchantAccountFulfilmentPointPspToken,
    PaymentCustomer, PaymentGateway, PaymentIntent, PaymentSource
)
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
    payment_customer = RelatedResourceLinkField(schema=PaymentCustomerSchema, data_key='paymentCustomer', microservice_aware=True, missing=None)
    token_provider = fields.String(data_key='tokenProvider')
    external_id = fields.String(data_key='externalId', missing=None)
    psp = fields.String(missing=None)
    type = fields.String()
    default = fields.Bool(missing=None)
    billing_details = fields.Dict(data_key='billingDetails', required=False, missing=None)
    card = fields.Dict()
    psp_tokens = fields.List(fields.Dict(), data_key='pspTokens')


class PaymentIntentSchema(Schema):
    class Meta:
        unknown = EXCLUDE
        api_type = 'payment_intents'
        url = 'payment/payment_intents'
        model = PaymentIntent

    id = fields.Int(missing=None)
    external_id = fields.String(data_key='externalId', missing=None, allow_none=True)
    payment_source = RelatedResourceLinkField(schema=PaymentSourceSchema, data_key='paymentSource', microservice_aware=True, missing=None)
    payment_customer = RelatedResourceLinkField(schema=PaymentCustomerSchema, data_key='paymentCustomer', microservice_aware=True, missing=None)
    status = fields.String()
    amount = fields.Int()
    currency = fields.String()
    last_payment_error = fields.String(data_key='lastPaymentError', missing=None)
    live_mode = fields.Bool(data_key='livemode')
    save_payment_source = fields.Bool(data_key='savePaymentSource')
    next_action = fields.Dict(data_key='nextAction', missing=None, allow_none=True)
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


class MerchantAccountFulfilmentPointSchema(Schema):
    class Meta:
        unknown = EXCLUDE
        api_type = 'merchant_account_fulfilment_points'
        url = 'payment/merchant_account_fulfilment_points'
        model = MerchantAccountFulfilmentPoint

    id = fields.Int(missing=None)
    merchant_account = RelatedResourceLinkField(schema=MerchantAccountSchema, data_key='merchantAccount', microservice_aware=True)
    fulfilment_point = RelatedResourceLinkField(schema=FulfilmentPointSchema, data_key='fulfilmentPoint', microservice_aware=True)


class MerchantAccountFulfilmentPointPspTokenSchema(Schema):
    class Meta:
        unknown = EXCLUDE
        api_type = 'merchant_account_fulfilment_point_psp_tokens'
        url = 'payment/merchant_account_fulfilment_point_psp_tokens'
        model = MerchantAccountFulfilmentPointPspToken

    id = fields.Int(missing=None)
    merchant_account_fulfilment_point = RelatedResourceLinkField(schema=MerchantAccountFulfilmentPointSchema, data_key='merchantAccountFulfilmentPoint', microservice_aware=True)
    payment_source = RelatedResourceLinkField(schema=PaymentSourceSchema, data_key='paymentSource', microservice_aware=True)
    psp_token = fields.String(data_key='pspToken')
