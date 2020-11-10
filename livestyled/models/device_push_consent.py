from livestyled.models.push_consent import PushConsent


class DevicePushConsent:
    def __init__(
            self,
            id: int,
            consent: bool,
            push_consent_id: str
    ):
        self.id = id
        self.consent = consent
        self._push_consent = PushConsent.placeholder(id=push_consent_id)

    @property
    def push_consent(self):
        return self._push_consent
