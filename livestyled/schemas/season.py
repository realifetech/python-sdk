from marshmallow import EXCLUDE, fields, Schema

from livestyled.models.season import Season


class SeasonSchema(Schema):
    class Meta:
        unknown = EXCLUDE
        api_type = 'seasons'
        url = 'v4/seasons'
        model = Season

    id = fields.Int()
    label = fields.String()
    name = fields.String()
    is_current = fields.Boolean(data_key='isCurrent')
    external_id = fields.String(data_key='externalId', missing=None)
