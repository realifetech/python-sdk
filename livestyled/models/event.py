from livestyled.models.event_date import EventDate
from livestyled.models.venue import Venue


class CoreEventCategory:
    def __init__(self, name):
        self.name = name


class Event:
    def __init__(
            self,
            id,
            status,
            title,
            description,
            promoted,
            updated_at,
            event_dates,
            created_at=None,
            translations=None,
            image_url=None,
            venues=None,
            core_event_category=None
    ):
        self._id = id
        self.status = status
        self.title = title
        self.description = description
        self.image_url = image_url
        self.promoted = promoted
        self.created_at = created_at
        self.updated_at = updated_at
        if event_dates:
            self.event_dates = [EventDate(**ed) for ed in event_dates]
        self.translations = translations
        if venues:
            self.venues = []
            for venue in venues:
                if isinstance(venue, dict):
                    self.venues.append(Venue(**venue))
                elif isinstance(venue, (str, int)):
                    self.venues.append(Venue.placeholder(id=venue))
                elif isinstance(venue, Venue):
                    self.venues.append(Venue)
        else:
            self.venues = []
        if core_event_category:
            if isinstance(core_event_category, dict):
                self.core_event_category = CoreEventCategory(name=core_event_category['name'])
            elif isinstance(core_event_category, CoreEventCategory):
                self.core_event_category = core_event_category
        else:
            self.core_event_category = CoreEventCategory(name='Other')

    @classmethod
    def placeholder(
            cls,
            id
    ):
        return cls(
            id=id,
            status=None,
            title=None,
            description=None,
            image_url=None,
            promoted=None,
            created_at=None,
            updated_at=None,
            event_dates=None,
            translations=None,
        )

    @property
    def id(self):
        return self._id

    def __repr__(self):
        return '<Event(id={self.id!r})>'.format(self=self)
