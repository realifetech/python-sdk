from marshmallow import EXCLUDE, fields, Schema

from livestyled.models.payment_customer import PaymentCustomer
from livestyled.schemas.fields import RelatedResourceLinkField
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
    payment_sources = fields.List()
