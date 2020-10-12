from marshmallow import EXCLUDE, fields, Schema

from livestyled.models.app import App, Currency


class CurrencySchema(Schema):
    class Meta:
        unknown = EXCLUDE
        model = Currency
        api_type = 'currencies'
        url = 'currencies'

    id = fields.Int(missing=None)
    title = fields.String(missing=None)
    iso_code = fields.String(missing=None, data_key='isoCode')
    sign = fields.String(missing=None)


class AppSchema(Schema):
    class Meta:
        unknown = EXCLUDE
        api_type = 'apps'
        url = 'apps'
        model = App

    id = fields.Int(missing=None)
    email = fields.Email(allow_none=True, missing=None)
    roles = fields.List(fields.String(), allow_none=True, missing=None)
    password = fields.String(missing=None)
    salt = fields.String(allow_none=True, missing=None)
    username = fields.String(missing=None)
    code = fields.String(missing=None)
    token = fields.String(missing=None)
    name = fields.String(missing=None)
    api_keys = fields.List(fields.String(), data_key='apiKeys', missing=None)
    timezone = fields.String(missing=None)
    google_api_key = fields.String(data_key='googleApiKey', allow_none=True, missing=None)
    payment_gateway = fields.String(data_key='paymentGateway', missing=None)
    venues = fields.List(fields.Inferred(), missing=None)  # TODO
    sender_email = fields.Email(data_key='senderEmail', missing=None)
    deeplink_namespace = fields.String(data_key='deeplinkNamespace', missing=None)
    merchant_accounts = fields.List(fields.Inferred, data_key='merchantAccounts', allow_none=True, missing=None)
    title = fields.String(missing=None)
    status = fields.String(missing=None)
    currency = fields.Nested(CurrencySchema, missing=None)
    cohorts = fields.List(fields.Inferred, missing=None)
