class DeviceConsent:
    def __init__(
            self,
            id: int,
            location_capture: bool,
            location_granular: bool,
            camera: bool,
            calendar: bool,
            photo_sharing: bool,
            push_notification: bool,
            created_at,
            updated_at
    ):
        self.id = id
        self.location_capture = location_capture
        self.location_granular = location_granular
        self.camera = camera
        self.calendar = calendar
        self.photo_sharing = photo_sharing
        self.push_notification = push_notification
        self.created_at = created_at
        self.updated_at = updated_at
