from collections import namedtuple
from datetime import datetime

from livestyled.models.competition import Competition
from livestyled.models.season import Season
from livestyled.models.sport_venue import SportVenue
from livestyled.models.team import Team


Score = namedtuple('Score', 'goals, penalties')
Url = namedtuple('Url', 'title, url, is_enabled')


class Fixture:
    def __init__(
            self,
            id,
            external_id,
            start_at,
            is_fulltime,
            is_terminated,
            home_id,
            away_id,
            home_score,
            away_score,
            season_id,
            competition_id,
            venue_id,
            status,
            url,
            allow_overwrite=False
    ):
        self._id = id
        self._external_id = external_id
        self._start_at = start_at
        self._is_fulltime = is_fulltime
        self._is_terminated = is_terminated
        self._home = Team.placeholder(id=home_id)
        self._away = Team.placeholder(id=away_id)
        self._home_goals = home_score['goals']
        self._home_penalties = home_score['penalties']
        self._away_goals = away_score['goals']
        self._away_penalties = away_score['penalties']
        self._season = Season.placeholder(id=season_id)
        self._competition = Competition.placeholder(id=competition_id)
        self._venue = SportVenue.placeholder(id=venue_id)
        self._status = status
        if url:
            if isinstance(url, Url):
                self.url = url
            elif isinstance(url, dict):
                self.url = Url(**url)
        else:
            self.url = None
        self.allow_overwrite = allow_overwrite

    @classmethod
    def create_new(
            cls,
            external_id: str,
            start_at: datetime,
            is_fulltime: bool,
            is_terminated: bool,
            home: Team or str or int,
            away: Team or str or int,
            home_goals: int or None,
            home_penalties: int or None,
            away_goals: int or None,
            away_penalties: int or None,
            season: Season or str or int,
            competition: Competition or str or int,
            venue: SportVenue or str or int,
            status: str,
            url: Url,
            allow_overwrite: bool = False,
    ):
        fixture = Fixture(
            id=None,
            external_id=external_id,
            start_at=start_at,
            is_fulltime=is_fulltime,
            is_terminated=is_terminated,
            home_id=None,
            away_id=None,
            home_score={'goals': home_goals, 'penalties': home_penalties},
            away_score={'goals': away_goals, 'penalties': away_penalties},
            season_id=None,
            competition_id=None,
            venue_id=None,
            status=status,
            url=url,
            allow_overwrite=allow_overwrite
        )
        if isinstance(home, (str, int)):
            home = Team.placeholder(id=home)
        fixture._home = home
        if isinstance(away, (str, int)):
            away = Team.placeholder(id=away)
        fixture._away = away
        if isinstance(season, (str, int)):
            season = Season.placeholder(id=season)
        fixture._season = season
        if isinstance(competition, (str, int)):
            competition = Competition.placeholder(id=competition)
        fixture._competition = competition
        if isinstance(venue, (str, int)):
            venue = SportVenue.placeholder(id=venue)
        fixture._venue = venue
        return fixture

    @property
    def id(self):
        return self._id

    @property
    def competition_id(self):
        return self._competition.id

    @property
    def home_id(self):
        return self._home.id

    @property
    def away_id(self):
        return self._away.id

    @property
    def home(self):
        return self._home

    @property
    def away(self):
        return self._away

    @property
    def season_id(self):
        return self._season.id

    @property
    def venue_id(self):
        return self._venue.id

    @property
    def home_score(self):
        return Score(
            goals=self._home_goals,
            penalties=self._home_penalties
        )

    @property
    def home_goals(self):
        return self._home_goals

    @home_goals.setter
    def home_goals(self, goals):
        self._home_goals = goals

    @property
    def away_score(self):
        return Score(
            goals=self._away_goals,
            penalties=self._away_penalties
        )

    @property
    def away_goals(self):
        return self._away_goals

    @away_goals.setter
    def away_goals(self, goals):
        self._away_goals = goals

    @property
    def status(self):
        return self._status

    @property
    def is_fulltime(self):
        return self._is_fulltime

    @property
    def is_terminated(self):
        return self._is_terminated

    @property
    def start_at(self):
        return self._start_at

    @property
    def external_id(self):
        return self._external_id

    @property
    def home_penalties(self):
        return self._home_penalties

    @property
    def away_penalties(self):
        return self._away_penalties

    def __repr__(self):
        return '<Fixture(id={self.id!r})>'.format(self=self)

    def diff(self, other):
        differences = {}
        fields = (
            'competition_id', 'home_id', 'away_id', 'season_id', 'venue_id',
            'home_score', 'away_score', 'status', 'is_fulltime', 'start_at', 'external_id', 'url',
            'allow_overwrite', 'is_terminated'
        )
        for field in fields:
            if getattr(self, field) != getattr(other, field):
                differences[field] = getattr(self, field)
        return differences
