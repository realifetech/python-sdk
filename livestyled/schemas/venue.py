from marshmallow import EXCLUDE, fields, post_load, Schema

from livestyled.models.venue import Venue


class VenueSchema(Schema):
    class Meta:
        unknown = EXCLUDE
        api_type = 'venues'
        url = 'event_management/venues'
        model = Venue

    id = fields.Int(missing=None)
    iri = fields.String(data_key='@id')
    name = fields.String()
    label = fields.String()
    status = fields.String()
    is_default = fields.Boolean(data_key='isDefault')
    description = fields.String(allow_none=True)
    image_url = fields.String(allow_none=True)
    map_image_url = fields.String(allow_none=True)
    geo_latitude = fields.String(allow_none=True)
    geo_longitude = fields.String(allow_none=True)
    geo_latitude_north_west = fields.String(allow_none=True)
    geo_longitude_north_west = fields.String(allow_none=True)
    geo_latitude_south_east = fields.String(allow_none=True)
    geo_longitude_south_west = fields.String(allow_none=True)
    city = fields.String(allow_none=True)
    external_id = fields.String(data_key='externalId', allow_none=True, missing=None)
    updated_at = fields.AwareDateTime(data_key='updatedAt', allow_none=True)
    created_at = fields.AwareDateTime(data_key='createdAt', allow_none=True)
    venue_icon_url = fields.String(data_key='venueIconUrl', allow_none=True)

    @post_load
    def fix_missing_id(self, data, **kwargs):
        if data['id'] is None:
            data['id'] = int(data['iri'].split('/')[-1])
        data.pop('iri', None)
        return data
