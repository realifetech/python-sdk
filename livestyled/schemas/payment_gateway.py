from marshmallow import EXCLUDE, fields, Schema

from livestyled.models.payment_gateway import PaymentGateway


class PaymentGateway(Schema):
    class Meta:
        unknown = EXCLUDE
        api_type = 'payment_gateways'
        url = 'payment/payment_gateways'
        model = PaymentGateway

    id = fields.Int(missing=None)
    config_ui_schema = fields.Dict(fields.String(), data_key='configUiSchema', allow_none=True)
    payment_gateway = fields.String(data_key='paymentGateway')
    name = fields.String()
