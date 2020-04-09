from marshmallow import EXCLUDE, fields, Schema

from livestyled.models.device_preference import DevicePreference


class DevicePreferenceSchema(Schema):
    class Meta:
        unknown = EXCLUDE
        model = DevicePreference
        api_type = 'device_preferences'
        url = 'v4/device_preferences'

    id = fields.Int()
    created_at = fields.String()
    device = fields.String()
    venue = fields.String()
    event = fields.String()
