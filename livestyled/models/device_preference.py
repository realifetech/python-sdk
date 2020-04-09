class DevicePreference:
    def __init__(
            self,
            id,
            created_at,
            device,
            venue,
            event,
    ):
        self._id = id
        self.created_at = created_at
        self.device = device
        self.venue = venue
        self.event = event

    @classmethod
    def create_new(
            cls,
            created_at: str,
            device: str,
            venue: str or None,
            event: str or None,
    ):
        return DevicePreference(
            id=None,
            device=device,
            venue=venue,
            event=event,
            created_at=created_at,
        )

    def __repr__(self):
        return '<DevicePreference(id={self.id!r}, device={self.device!r}, venue={self.venue!r}, event={self.event!r})>'\
            .format(self=self)
