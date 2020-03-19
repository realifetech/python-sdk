from marshmallow import EXCLUDE, fields, Schema

from livestyled.models.league_table import LeagueTable, LeagueTableGroup
from livestyled.schemas.competition import CompetitionSchema
from livestyled.schemas.fields import RelatedResourceLinkField
from livestyled.schemas.season import SeasonSchema
from livestyled.schemas.team import TeamSchema


class LeagueTableGroupSchema(Schema):
    class Meta:
        unknown = EXCLUDE
        api_type = 'league_table_groups'
        url = 'v4/league_table_groups'
        model = LeagueTableGroup

    id = fields.Int(required=False, allow_none=False)
    reference = fields.String(required=True, allow_none=True)
    title = fields.String(required=True, allow_none=True)


class LeagueTableSchema(Schema):
    class Meta:
        unknown = EXCLUDE
        api_type = 'league_tables'
        url = 'v4/league_tables'
        model = LeagueTable

    id = fields.Int(required=False, allow_none=False)
    team_id = RelatedResourceLinkField(schema=TeamSchema, data_key='team')
    external_id = fields.String(required=True, allow_none=True, data_key='externalId')
    featured_team = fields.Boolean(required=True, allow_none=False, data_key='featuredTeam')
    position = fields.Int(missing=0)
    played = fields.Int(missing=0)
    goals_for = fields.Int(data_key='goalsFor', missing=0)
    goals_against = fields.Int(data_key='goalsAgainst', missing=0)
    start_day_position = fields.Int(data_key='startDayPosition', missing=0)
    won = fields.Int(missing=0)
    lost = fields.Int(missing=0)
    drawn = fields.Int(missing=0)
    goal_difference = fields.Int(data_key='goalDifference', missing=0)
    points = fields.Int(missing=0)
    competition_id = RelatedResourceLinkField(schema=CompetitionSchema, data_key='competition')
    season_id = RelatedResourceLinkField(schema=SeasonSchema, data_key='season')
    group_id = RelatedResourceLinkField(schema=LeagueTableGroupSchema, data_key='group')
