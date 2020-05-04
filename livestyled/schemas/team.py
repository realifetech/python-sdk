from marshmallow import EXCLUDE, fields, Schema

from livestyled.models.team import Team


class TeamSchema(Schema):
    class Meta:
        unknown = EXCLUDE
        api_type = 'teams'
        url = 'v4/teams'
        model = Team

    id = fields.Int(required=False, allow_none=False)
    name = fields.String(data_key='name')
    short_name = fields.String(data_key='shortName')
    light_crest_url = fields.String(data_key='lightCrestUrl', missing=None)
    dark_crest_url = fields.String(data_key='darkCrestUrl', missing=None)
    external_id = fields.String(data_key='externalId', missing=None)
