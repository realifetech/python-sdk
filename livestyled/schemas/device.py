from marshmallow import EXCLUDE, fields, Schema


class DeviceSchema(Schema):
    class Meta:
        unknown = EXCLUDE
        api_type = 'devices'
        url = 'v4/devices'

    id = fields.Int()
    token = fields.String()
    consent = fields.Nested('livestyled.schemas.device_consent.DeviceConsentSchema', allow_none=True)
    push_consents = fields.List(fields.Dict, data_key='pushConsents', allow_none=True)  # TODO
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
