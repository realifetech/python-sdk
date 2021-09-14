from datetime import datetime

from livestyled.models.payment_customer import PaymentCustomer


class PaymentSource:
    def __init__(
            self,
            id: int,
            status: str,
            payment_customer: str or None,
            token_provider: str,
            external_id: str,
            psp: str,
            type: str,
            default: bool,
            billing_details: dict,
            card: dict,
            psp_tokens: [],
            created_at: datetime or None = None,
            updated_at: datetime or None = None

    ):
        self.id = id
        self.status = status
        self.payment_customer = PaymentCustomer.placeholder(id=payment_customer)
        self.token_provider = token_provider
        self.external_id = external_id
        self.type = type
        self.default = default
        self.billing_details = billing_details
        self.card = card
        self.psp_tokens = psp_tokens
        self.created_at = created_at
        self.updated_at = updated_at

    @classmethod
    def create_new(
            cls,
            status: str,
            payment_customer: str,
            token_provider: str,
            external_id: str,
            type: str,
            default: str,
            billing_details: dict,
            card: dict,
            psp_tokens: []
    ):
        if isinstance(payment_customer, (str, int)):
            payment_customer = PaymentCustomer.placeholder(id=payment_customer)

        return PaymentSource(
            id=None,
            status=status,
            payment_customer=payment_customer,
            token_provider=token_provider,
            external_id=external_id,
            type=type,
            default=default,
            billing_details=billing_details,
            card=card,
            psp_tokens=psp_tokens
        )

    @classmethod
    def placeholder(
            cls,
            id
    ):
        return cls(
            id=id,
            status=None,
            payment_customer=None,
            token_provider=None,
            external_id=None,
            type=None,
            default=None,
            billing_details=None,
            card=None,
            psp_tokens=[]
        )

    def diff(self, other):
        differences = {}
        fields = (
            'status', 'payment_customer', 'token_provider', 'external_id', 'type', 'default', 'billing_details', 'card', 'psp_tokens'
        )
        for field in fields:
            if getattr(self, field) != getattr(other, field):
                differences[field] = getattr(self, field)
        return differences

    @property
    def payment_customer_id(self):
        return self._payment_customer.id

    @property
    def payment_customer(self):
        return self._payment_customer
