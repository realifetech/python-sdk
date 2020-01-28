from marshmallow import EXCLUDE, fields, Schema


class TeamSchema(Schema):
    class Meta:
        unknown = EXCLUDE
        api_type = 'teams'
        url = 'v4/teams'

    id = fields.Int()
    name = fields.String(data_key='name')
    short_name = fields.String(data_key='shortName')
    light_crest_url = fields.URL(data_key='lightCrestURL', allow_none=True)
    dark_crest_url = fields.URL(data_key='darkCrestURL')
    external_id = fields.String(data_key='externalId')
