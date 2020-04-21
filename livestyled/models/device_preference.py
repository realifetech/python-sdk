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
        if venue_id:
            self._venue = Venue.placeholder(id=venue_id)
        else:
            self._venue = None
        if event_id:
            self._event = Event.placeholder(id=event_id)
        else:
            self._event = None

    @classmethod
    def create_new(
            cls,
            device: Device or str or int,
            venue: Venue or str or int or None,
            event: Event or str or int,
    ):
        device_pref = DevicePreference(
            id=None,
            device_id=None,
            venue_id=None,
            event_id=None,
            created_at=None,
        )
        if isinstance(event, (str, int)):
            event = Event.placeholder(event)
        device_pref._event = event
        if isinstance(device, (str, int)):
            device = Device.placeholder(id=device)
        device_pref._device = device
        if isinstance(venue, (str, int)):
            venue = Venue.placeholder(id=venue)
        device_pref._venue = venue
        return device_pref

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
    def event_id(self):
        return self._event.id

    @property
    def event(self):
        return self._event

    @property
    def venue_id(self):
        return self._venue.id

    @property
    def venue(self):
        return self._venue

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
