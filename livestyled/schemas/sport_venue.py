from marshmallow import EXCLUDE, fields, Schema

from livestyled.models.sport_venue import SportVenue


class SportVenueSchema(Schema):
    class Meta:
        unknown = EXCLUDE
        api_type = 'sport_venues'
        url = 'sport_venues'
        model = SportVenue
        include_v4_in_iri = True

    id = fields.Int()
    name = fields.String()
