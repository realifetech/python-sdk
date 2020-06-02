from marshmallow import EXCLUDE, fields, Schema

from livestyled.models import Device, DevicePushConsent
from livestyled.schemas.device_consent import DeviceConsentSchema
from livestyled.schemas.fields import RelatedResourceField, RelatedResourceLinkField
from livestyled.schemas.push_consent import PushConsentSchema


class DevicePushConsentSchema(Schema):
    class Meta:
        unknown = EXCLUDE
        model = DevicePushConsent

    id = fields.Int()
    consent = fields.Boolean()
    push_consent_id = RelatedResourceLinkField(schema=PushConsentSchema, data_key='pushConsent')


class DeviceSchema(Schema):
    class Meta:
        unknown = EXCLUDE
        api_type = 'devices'
        url = 'v4/devices'
        model = Device

    id = fields.Int()
    token = fields.String()
    consent = RelatedResourceField(schema=DeviceConsentSchema, allow_none=True, missing=None)
    push_consents = RelatedResourceField(schema=DevicePushConsentSchema, many=True, data_key='pushConsents', required=False, missing=None)
    type = fields.String()
    status = fields.String()
    app_version = fields.String(data_key='appVersion')
    os_version = fields.String(data_key='osVersion', allow_none=True)
    model = fields.String(allow_none=True)
    manufacturer = fields.String(allow_none=True)
    bluetooth_on = fields.Boolean(data_key='bluetoothOn', allow_none=True)
    wifi_connected = fields.Boolean(data_key='wifiConnected', allow_none=True)
    updated_at = fields.AwareDateTime(data_key='updatedAt', allow_none=True)
    created_at = fields.AwareDateTime(data_key='createdAt', allow_none=True)
