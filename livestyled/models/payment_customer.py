from datetime import datetime

from livestyled.models.user import User


class PaymentCustomer:
    def __init__(
            self,
            id: int,
            user: str or None,
            external_ids: dict,
            payment_sources: [],
            created_at: datetime or None = None,
            updated_at: datetime or None = None

    ):
        self.id = id
        self.user = User.placeholder(id=user)
        self.external_ids = external_ids
        self.payment_sources = payment_sources
        self.created_at = created_at
        self.updated_at = updated_at

    @classmethod
    def create_new(
            cls,
            user: str,
            external_ids: dict,
            payment_sources: []
    ):
        if isinstance(user, (str, int)):
            user = User.placeholder(id=user)

        return PaymentCustomer(
            id=None,
            user=user,
            external_ids=external_ids,
            payment_sources=payment_sources
        )

    @classmethod
    def placeholder(
            cls,
            id
    ):
        return cls(
            id=id,
            user=None,
            external_ids=None,
            payment_sources=[]
        )

    def diff(self, other):
        differences = {}
        fields = (
            'user', 'external_ids', 'payment_sources'
        )
        for field in fields:
            if getattr(self, field) != getattr(other, field):
                differences[field] = getattr(self, field)
        return differences

    @property
    def user_id(self):
        return self._user.id

    @property
    def user(self):
        return self._user
