from marshmallow import EXCLUDE, fields, Schema

from livestyled.models import Location


class LocationPolygon(Schema):
    class Meta:
        unknown = EXCLUDE

    coordinates = fields.List(fields.List(fields.List(fields.Float())))


class LocationCoordinates(Schema):
    class Meta:
        unknown = EXCLUDE

    lat = fields.String(allow_none=True)
    lon = fields.String(allow_none=True)


class LocationSchema(Schema):
    class Meta:
        unknown = EXCLUDE
        api_type = 'locations'
        url = 'user_management/locations'
        model = Location

    id = fields.Int()
    status = fields.String()
    listed = fields.Boolean()
    name = fields.String(allow_none=True)
    coordinates = fields.Nested(LocationCoordinates, allow_none=True)
    polygon = fields.Nested(LocationPolygon, allow_none=True)
    sort_id = fields.Int(data_key='sortId')
    external_id = fields.String(data_key='externalId', allow_none=True, blank=True)
