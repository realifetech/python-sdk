from marshmallow import EXCLUDE, fields, Schema

from livestyled.models.currency import Currency


class CurrencySchema(Schema):
    class Meta:
        unknown = EXCLUDE
        api_type = 'currencies'
        url = 'currencies'
        model = Currency

    id = fields.Int()
    title = fields.String()
    iso_code = fields.String(data_key='isoCode')
    sign = fields.String()
