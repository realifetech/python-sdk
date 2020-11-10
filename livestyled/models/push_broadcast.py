from livestyled.models.push_consent import PushConsent


class PushBroadcast:
    def __init__(
            self,
            id: int or None,
            title: str or None,
            message,
            message_id,
            updated_at,
            created_at,
            delivered=None,
            push_consent_id=None,
            deep_link=None,
            ttl=None,
    ):
        self.id = id
        self.title = title
        self.message = message
        self.deep_link = deep_link
        self.ttl = ttl
        self.message_id = message_id
        self.delivered = delivered
        self.updated_at = updated_at
        self.created_at = created_at
        if push_consent_id:
            self._push_consent = PushConsent.placeholder(id=push_consent_id)
        else:
            self._push_consent = None

    @classmethod
    def create_new(
            cls,
            title,
            message,
            deep_link,
            ttl=0,
            message_id=None,
            delivered=0,
            updated_at=None,
            created_at=None,
            push_consent=None
    ):
        push_broadcast = PushBroadcast(
            id=None,
            title=title,
            message=message,
            deep_link=deep_link,
            ttl=ttl,
            message_id=message_id,
            delivered=delivered,
            updated_at=updated_at,
            created_at=created_at,
            push_consent_id=None
        )
        push_broadcast._push_consent = push_consent
        return push_broadcast

    @classmethod
    def placeholder(
            cls,
            id
    ):
        return cls(
            id=id,
            title=None,
            message=None,
            deep_link=None,
            ttl=None,
            message_id=None,
            delivered=None,
            updated_at=None,
            created_at=None,
            push_consent_id=None
        )

    @property
    def push_consent_id(self):
        return self._push_consent.id

    @property
    def push_consent(self):
        return self._push_consent

    def diff(self, other):
        differences = {}
        fields = (
            'title', 'message', 'deep_link', 'ttl', 'message_id', 'delivered',
            'updated_at', 'created_at', 'push_consent_id'
        )
        for field in fields:
            if getattr(self, field) != getattr(other, field):
                differences[field] = getattr(self, field)
        return differences
