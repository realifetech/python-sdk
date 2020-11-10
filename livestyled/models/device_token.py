from livestyled.models.device import Device


class DeviceToken:
    def __init__(
            self,
            id: int or None,
            provider: str,
            provider_token: str,
            payload,
            device_id: str or None = None
    ):
        self._id = id
        self.provider = provider
        self.provider_token = provider_token
        self.payload = payload
        self._device = Device.placeholder(id=device_id)

    @property
    def id(self):
        return self._id

    @classmethod
    def create_new(
            cls,
            provider,
            provider_token,
            payload,
            device
    ):
        token = DeviceToken(
            id=None,
            provider=provider,
            provider_token=provider_token,
            payload=payload,
            device_id=None
        )
        if isinstance(device, (str, int)):
            device = Device.placeholder(id=device)
        token._device = device
        return token

    def __repr__(self):
        return '<DeviceToken(id={self.id!r}, provider={self.provider!r})>'.format(self=self)

    def diff(self, other):
        differences = {}
        fields = (
            'provider', 'provider_token', 'payload',
        )
        for field in fields:
            if getattr(self, field) != getattr(other, field):
                differences[field] = getattr(self, field)
        return differences

    @property
    def device_id(self):
        return self._device.id

    @property
    def device(self):
        return self._device
