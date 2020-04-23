from datetime import datetime
from typing import Dict, List

from livestyled.models.device_consent import DeviceConsent
from livestyled.models.device_push_consent import DevicePushConsent


class Device:
    def __init__(
            self,
            id: int,
            token: str,
            consent: Dict,
            push_consents: List[Dict],
            type: str,
            status: str,
            app_version: str,
            os_version: str,
            model: str,
            manufacturer: str,
            bluetooth_on: bool,
            wifi_connected: bool,
            updated_at: datetime,
            created_at: datetime,
    ):
        self._id = id
        self.token = token
        if consent:
            self.consent = DeviceConsent(**consent)
        else:
            self.consent = None
        if push_consents:
            self.push_consents = [DevicePushConsent(**dpc) for dpc in push_consents]
        else:
            self.push_consents = []
        self.type = type
        self.status = status
        self.app_version = app_version
        self.os_version = os_version
        self.model = model
        self.manufacturer = manufacturer
        self.bluetooth_on = bluetooth_on
        self.wifi_connected = wifi_connected
        self.created_at = created_at
        self.updated_at = updated_at

    @property
    def id(self):
        return self._id

    @classmethod
    def placeholder(
            cls,
            id
    ):
        return cls(
            id=id,
            token=None,
            consent=None,
            push_consents=None,
            type=None,
            status=None,
            app_version=None,
            os_version=None,
            model=None,
            manufacturer=None,
            bluetooth_on=None,
            wifi_connected=None,
            updated_at=None,
            created_at=None,
        )

    def __repr__(self):
        return '<Device(id={self.id!r})>'.format(self=self)
