from marshmallow import EXCLUDE, fields, Schema

from livestyled.models import Export


class ExportSchema(Schema):
    class Meta:
        unknown = EXCLUDE
        api_type = 'exports'
        url = 'storage/exports'
        model = Export

    id = fields.Int(missing=None)
    status = fields.String(allow_none=True)
    type = fields.String(allow_none=True)
    filters = fields.Dict(allow_none=True)
    url = fields.String(missing=None)
    owner = fields.Int(missing=None)
