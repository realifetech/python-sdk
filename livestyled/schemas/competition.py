from marshmallow import EXCLUDE, fields, Schema

from livestyled.models.competition import Competition


class CompetitionSchema(Schema):
    class Meta:
        unknown = EXCLUDE
        api_type = 'competitons'
        url = 'v4/competitions'
        model = Competition

    id = fields.Int()
    label = fields.String()
    name = fields.String()
    status = fields.String(allow_none=True)
    external_id = fields.String(data_key='externalId', missing=None)
    logo_url = fields.String(data_key='logoUrl', allow_none=True)
    sort_id = fields.Int(data_key='sortId')
