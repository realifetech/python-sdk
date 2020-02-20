from marshmallow import EXCLUDE, fields, post_load, Schema

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
    light_crest_url = fields.URL(data_key='lightCrestUrl')
    external_id = fields.String(data_key='externalId', missing=None)
