from marshmallow import EXCLUDE, fields, Schema

from livestyled.models.device_consent import DeviceConsent


class DeviceConsentSchema(Schema):
    class Meta:
        unknown = EXCLUDE
        model = DeviceConsent

    id = fields.Int()
    location_capture = fields.Boolean(data_key='locationCapture', allow_none=True)
    location_granular = fields.String(data_key='locationGranular', allow_none=True)
    camera = fields.Boolean(data_key='camera', allow_none=True)
    calendar = fields.Boolean(allow_none=True)
    photo_sharing = fields.Boolean(data_key='photoSharing', allow_none=True)
    push_notification = fields.Boolean(data_key='pushNotification', allow_none=True)
    updated_at = fields.AwareDateTime(data_key='updatedAt', allow_none=True)
    created_at = fields.AwareDateTime(data_key='createdAt', allow_none=True)
