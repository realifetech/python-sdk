from datetime import datetime
from typing import Dict

from livestyled.models.audience import Audience
from livestyled.models.device import Device


class AudienceDevice:
    def __init__(
            self,
            audience: Dict or Audience,
            device: Dict or Device,
            created_at: datetime or None = None
    ):
        self.created_at = created_at
        if isinstance(audience, Audience):
            self.audience = audience
        elif isinstance(audience, int):
            self.audience = Audience.placeholder(id=audience)
        else:
            self.audience = Audience(**audience)
        if isinstance(device, Device):
            self.device = device
        elif isinstance(device, int):
            self.device = Device.placeholder(id=device)
        else:
            self.device = Device(**device)

    @property
    def id(self):
        return 'device={};audience={}'.format(self.device.id, self.audience.id)

    @property
    def compound_id(self):
        return True
