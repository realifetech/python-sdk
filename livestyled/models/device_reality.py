from datetime import datetime

from livestyled.models.device import Device
from livestyled.models.reality import Reality


class DeviceReality:
    def __init__(
            self,
            id,
            device: Device or str,
            reality: Reality or str,
            value: str,
            created_at: datetime,
            updated_at: datetime,
    ):
        self.id = id
        self.value = value
        self.created_at = created_at
        self.updated_at = updated_at

        if device:
            if isinstance(device, Device):
                self.device = device
            elif isinstance(device, dict):
                self.device = Device(**device)
            elif isinstance(device, int):
                self.device = Device.placeholder(id=device)
        else:
            self.device = None

        if reality:
            if isinstance(reality, Reality):
                self.reality = reality
            elif isinstance(reality, dict):
                self.reality = Reality(**reality)
            elif isinstance(reality, int):
                self.reality = Reality.placeholder(id=reality)
        else:
            self.reality = None

    @classmethod
    def placeholder(cls, id):
        return cls(
            id,
            device=None,
            reality=None,
            value=None,
            created_at=None,
            updated_at=None
        )

    @classmethod
    def create_new(
            cls,
            device: Device,
            reality: Reality,
            value: str
    ):
        device_reality = DeviceReality(
            id=None,
            device=device,
            reality=reality,
            value=value,
            created_at=None,
            updated_at=None,
        )
        return device_reality

    def diff(self, other):
        differences = {}
        fields = (
            'value'
        )
        for field in fields:
            if getattr(self, field) != getattr(other, field):
                differences[field] = getattr(self, field)
        return differences
