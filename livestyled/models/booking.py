class Booking:
    def __init__(
            self,
            id,
            type,
            device,
            user,
            event,
            created_at,
            updated_at,
            action,
    ):
        self._id = id
        self.type = type
        self.device = device
        self.user = user
        self.event = event
        self.created_at = created_at
        self.updated_at = updated_at
        self.action = action

    @classmethod
    def create_new(
            cls,
            type: str,
            device: str,
            user: str or None,
            event: str,
            created_at: str,
            updated_at: str,
            action: str,
    ):
        return Booking(
            id=None,
            type=type,
            device=device,
            user=user,
            event=event,
            created_at=created_at,
            updated_at=updated_at,
            action=action,
        )

    def __repr__(self):
        return '<Booking(id={self.id!r}, type={self.type!r}, action={self.action!r})>'.format(self=self)
