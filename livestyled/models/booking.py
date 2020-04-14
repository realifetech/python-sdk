from livestyled.models.device import Device
from livestyled.models.event import Event
from livestyled.models.user import User


class Booking:
    def __init__(
            self,
            id,
            type,
            device_id,
            event_id,
            created_at,
            updated_at,
            action,
            user_id=None,
    ):
        self._id = id
        self.type = type
        self._device = Device.placeholder(id=device_id)
        if user_id:
            self._user = User.placeholder(id=user_id)
        else:
            self._user = None
        self._event = Event.placeholder(id=event_id)
        self.created_at = created_at
        self.updated_at = updated_at
        self.action = action

    @classmethod
    def create_new(
            cls,
            type: str,
            device: Device,
            user: User or None,
            event: Event,
            created_at: str,
            updated_at: str,
            action: str,
    ):
        booking = Booking(
            id=None,
            type=type,
            device_id=None,
            user_id=None,
            event_id=None,
            created_at=created_at,
            updated_at=updated_at,
            action=action,
        )
        booking._user = user
        booking._device = device
        booking._event = event
        return booking

    @property
    def id(self):
        return self._id

    @property
    def device_id(self):
        return self._device.id

    @property
    def device(self):
        return self._device

    @property
    def user_id(self):
        if self._user:
            return self._user.id
        else:
            return None

    @property
    def user(self):
        return self._user

    @property
    def event_id(self):
        return self._event.id

    @property
    def event(self):
        return self._event

    def __repr__(self):
        return '<Booking(id={self.id!r}, type={self.type!r}, action={self.action!r})>'.format(self=self)

    def diff(self, other):
        differences = {}
        fields = (
            'device_id', 'user_id', 'event_id', 'type', 'action'
        )
        for field in fields:
            if getattr(self, field) != getattr(other, field):
                differences[field] = getattr(self, field)
        return differences
