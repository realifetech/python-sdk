from marshmallow import EXCLUDE, fields, Schema

from livestyled.models.fixture import Fixture
from livestyled.schemas.competition import CompetitionSchema
from livestyled.schemas.fields import RelatedResourceLinkField
from livestyled.schemas.season import SeasonSchema
from livestyled.schemas.sport_venue import SportVenueSchema
from livestyled.schemas.team import TeamSchema


class FixtureSchema(Schema):
    class Meta:
        unknown = EXCLUDE
        api_type = 'fixtures'
        url = 'v4/fixtures'
        model = Fixture

    class ScoreSchema(Schema):
        goals = fields.Int(allow_none=True)
        penalties = fields.Int(allow_none=True)

    class FixtureUrlSchema(Schema):
        class Meta:
            unknown = EXCLUDE

        title = fields.String(allow_none=True)
        url = fields.String(allow_none=True)
        is_enabled = fields.Boolean()

    id = fields.Int(load_only=True)
    start_at = fields.DateTime(data_key='startAt')
    is_fulltime = fields.Boolean(data_key='isFullTime')
    is_terminated = fields.Boolean(data_key='isTerminated')
    home_id = RelatedResourceLinkField(schema=TeamSchema, data_key='home')
    away_id = RelatedResourceLinkField(schema=TeamSchema, data_key='away')
    home_score = fields.Nested(ScoreSchema, data_key='homeScore')
    away_score = fields.Nested(ScoreSchema, data_key='awayScore')
    season_id = RelatedResourceLinkField(schema=SeasonSchema, data_key='season')
    competition_id = RelatedResourceLinkField(schema=CompetitionSchema, data_key='competition')
    venue_id = RelatedResourceLinkField(schema=SportVenueSchema, data_key='sportVenue')
    external_id = fields.String(missing=None, data_key='externalId')
    status = fields.String()
    url = fields.Nested(FixtureUrlSchema, allow_none=True, missing=None)
    allow_overwrite = fields.Boolean(data_key='allowOverwrite')
