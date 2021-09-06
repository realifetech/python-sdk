from marshmallow import EXCLUDE, fields, Schema

class PaymentGateway(Schema):
    class Meta:
        unknown = EXCLUDE
        api_type = 'payment_gateways'
        url = 'payment/payment_gateways'
        model = PaymentGateway

    id = fields.Int(missing=None)
    config_ui_schema = fields.List(data_key='configUiSchema', allow_none=True)
    payment_gateway = field.String(data_key='paymentGateway')
    name = field.String()
