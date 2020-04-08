from .event_date import EventDate


class Event:
    def __init__(
            self,
            id,
            status,
            title,
            description,
            image_url,
            promoted,
            created_at,
            updated_at,
            event_dates,
            translations,
    ):
        self._id = id
        self._status = status
        self._title = title
        self._description = description
        self._image_url = image_url
        self._promoted = promoted
        self._created_at = created_at
        self._updated_at = updated_at
        if event_dates:
            self._event_dates = [EventDate(**ed) for ed in event_dates]
        self._translations = translations


    @property
    def id(self):
        return self._id


    def __repr__(self):
        return '<Event(id={self.id!r})>'.format(self=self)
