from marshmallow import EXCLUDE, fields, Schema


class AppSchema(Schema):
    class Meta:
        unknown = EXCLUDE
        api_type = 'apps'
        url = 'v4/apps'

    id = fields.Int()
    email = fields.Email(allow_none=True)
    roles = fields.List(fields.String(), allow_none=True)
    password = fields.String()
    salt = fields.String(allow_none=True)
    username = fields.String()
    code = fields.String()
    token = fields.String()
    name = fields.String()
    api_keys = fields.List(fields.String(), data_key='apiKeys')
    timezone = fields.String()
    google_api_key = fields.String(data_key='googleApiKey', allow_none=True)
    payment_gateway = fields.String(data_key='paymentGateway')
    venues = fields.List(fields.Inferred())  # TODO
    sender_email = fields.Email(data_key='senderEmail')
    deeplink_namespace = fields.String(data_key='deeplinkNamespace')
    merchant_accounts = fields.List(fields.Inferred, data_key='merchantAccounts', allow_none=True)
    title = fields.String()
    status = fields.String()
    currency = fields.Dict()  # TODO
    cohorts = fields.List(fields.Inferred)
