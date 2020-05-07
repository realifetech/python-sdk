from livestyled.models.competition import Competition
from livestyled.models.season import Season
from livestyled.models.team import Team


class LeagueTableGroup:
    def __init__(
            self,
            id,
            reference,
            title,
    ):
        self._id = id
        self._reference = reference
        self._title = title

    @classmethod
    def create_new(
            cls,
            reference,
            title
    ):
        return LeagueTableGroup(
            id=None,
            reference=reference,
            title=title
        )

    @property
    def id(self):
        return self._id

    @property
    def reference(self):
        return self._reference

    @property
    def title(self):
        return self._title

    @classmethod
    def placeholder(
            cls,
            id
    ):
        return cls(
            id=id,
            reference=None,
            title=None
        )

    def __repr__(self):
        return '<LeagueTableGroup(id={self.id!r})>'.format(self=self)

    def diff(self, other):
        differences = {}
        fields = (
            'reference', 'title'
        )
        for field in fields:
            if getattr(self, field) != getattr(other, field):
                differences[field] = getattr(self, field)
        return differences


class LeagueTable:
    def __init__(
            self,
            id,
            external_id,
            team_id,
            featured_team,
            position,
            played,
            goals_for,
            goals_against,
            start_day_position,
            won,
            lost,
            drawn,
            goal_difference,
            points,
            competition_id,
            season_id,
            group_id=None
    ):
        self._id = id
        self.external_id = external_id
        self._team = Team.placeholder(id=team_id)
        self._season = Season.placeholder(id=season_id)
        self._competition = Competition.placeholder(id=competition_id)
        if group_id:
            self._group = LeagueTableGroup.placeholder(id=group_id)
        else:
            self._group = None
        self.featured_team = featured_team
        self.position = position
        self.played = played
        self.goals_for = goals_for
        self.goals_against = goals_against
        self.start_day_position = start_day_position
        self.won = won
        self.lost = lost
        self.drawn = drawn
        self.goal_difference = goal_difference
        self.points = points

    @classmethod
    def create_new(
            cls,
            external_id,
            team: Team,
            featured_team,
            position,
            played,
            goals_for,
            goals_against,
            start_day_position,
            won,
            lost,
            drawn,
            goal_difference,
            points,
            competition: Competition,
            season: Season,
            group
    ):
        league_table = LeagueTable(
            id=None,
            external_id=external_id,
            featured_team=featured_team,
            position=position,
            played=played,
            goals_for=goals_for,
            goals_against=goals_against,
            start_day_position=start_day_position,
            won=won,
            lost=lost,
            drawn=drawn,
            goal_difference=goal_difference,
            points=points,
            season_id=None,
            competition_id=None,
            group_id=None,
            team_id=None
        )
        league_table._team = team
        league_table._season = season
        league_table._competition = competition
        league_table._group = group
        return league_table

    @property
    def id(self):
        return self._id

    @property
    def competition_id(self):
        return self._competition.id

    @property
    def team_id(self):
        return self._team.id

    @property
    def season_id(self):
        return self._season.id

    @property
    def group_id(self):
        if self._group:
            return self._group.id
        else:
            return None

    def __repr__(self):
        return '<LeagueTable(id={self.id!r})>'.format(self=self)

    def diff(self, other):
        differences = {}
        fields = (
            'competition_id', 'team_id', 'group_id', 'season_id',
            'featured_team', 'position', 'played', 'goals_for', 'goals_against', 'external_id',
            'start_day_position', 'won', 'lost', 'drawn', 'goal_difference', 'points'
        )
        for field in fields:
            if getattr(self, field) != getattr(other, field):
                differences[field] = getattr(self, field)
        return differences
