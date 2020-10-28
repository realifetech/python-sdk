class EventDate:
    def __init__(
            self,
            id,
            start_at,
            end_at,
            general_ticket_url=None,
    ):
        self._id = id
        self.start_at = start_at
        self.end_at = end_at
        self.general_ticket_url = general_ticket_url

    @classmethod
    def placeholder(
            cls,
            id
    ):
        return cls(
            id=id,
            start_at=None,
            end_at=None,
            general_ticket_url=None
        )

    @property
    def id(self):
        return self._id

    def __repr__(self):
        return '<EventDate(id={self.id!r})>'.format(self=self)
