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

    @property
    def id(self):
        return self._id

    def __repr__(self):
        return '<Event(id={self.id!r})>'.format(self=self)
