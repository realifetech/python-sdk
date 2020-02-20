from marshmallow import EXCLUDE, fields, Schema

from livestyled.models.sport_venue import SportVenue


class SportVenueSchema(Schema):
    class Meta:
        unknown = EXCLUDE
        api_type = 'sport_venues'
        url = 'v4/sport_venues'
        model = SportVenue

    id = fields.Int()
    name = fields.String()
