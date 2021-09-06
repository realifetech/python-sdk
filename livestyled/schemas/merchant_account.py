from marshmallow import EXCLUDE, fields, Schema

from livestyled.models.merchant_account import MerchantAccount
from livestyled.schemas.fields import RelatedResourceField, RelatedResourceLinkField
from livestyled.schemas.payment_gateway import PaymentGatewaySchema


class MerchantAccount(Schema):
    class Meta:
        unknown = EXCLUDE
        api_type = 'merchant_accounts'
        url = 'payment/merchant_accounts'
        model = MerchantAccount

    id = fields.Int(missing=None)
    status = fields.String()
    payment_gateway_id = RelatedResourceLinkField(schema=PaymentGatewaySchema, data_key='paymentGateway', microservice_aware=True)
    config = fields.List(allow_none=True)
    label = fields.String()
    fulfilment_points = RelatedResourceField(schema=FulfilmentPointSchema, many=True, data_key='fulfilmentPoints')
