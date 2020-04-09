from livestyled.models.device import Device
from livestyled.models.event import Event
from livestyled.models.venue import Venue


class DevicePreference:
    def __init__(
            self,
            id,
            created_at,
            device_id,
            venue_id,
            event_id,
    ):
        self._id = id
        self.created_at = created_at
        self._device = Device.placeholder(id=device_id)
        self._venue = Venue.placeholder(id=venue_id)
        self._event = Event.placeholder(id=event_id)

    @classmethod
    def create_new(
            cls,
            created_at: str,
            device: Device,
            venue: Venue or None,
            event: Event,
    ):
        device_pref = DevicePreference(
            id=None,
            device_id=None,
            venue_id=None,
            event_id=None,
            created_at=created_at,
        )
        device_pref._event = event
        device_pref._device = device
        device_pref._venue = venue
        return device_pref

    @property
    def device_id(self):
        return self._device.id

    @property
    def device(self):
        return self._device

    @property
    def event_id(self):
        return self._event.id

    @property
    def event(self):
        return self._event

    @property
    def venue_id(self):
        if self._venue:
            return self._venue.id
        else:
            return None

    @property
    def venue(self):
        return self.venue

    def __repr__(self):
        return '<DevicePreference(id={self.id!r}, device={self.device!r}, venue={self.venue!r}, event={self.event!r})>'.format(self=self)

    def diff(self, other):
        differences = {}
        fields = (
            'device_id', 'venue_id', 'event_id',
        )
        for field in fields:
            if getattr(self, field) != getattr(other, field):
                differences[field] = getattr(self, field)
        return differences
