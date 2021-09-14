from marshmallow import EXCLUDE, fields, Schema

from livestyled.models.payment_source import PaymentSource
from livestyled.schemas.fields import RelatedResourceLinkField
from livestyled.schemas.payment_customer import PaymentCustomerSchema


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
