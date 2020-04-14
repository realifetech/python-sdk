from .event_date import EventDate


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
