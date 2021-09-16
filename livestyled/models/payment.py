from datetime import datetime

from livestyled.models.fulfilment_point import FulfilmentPoint
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


class PaymentGateway:
    def __init__(
        self,
        id: int,
        config_ui_schema: dict,
        payment_gateway: str,
        name: str,
        created_at: datetime or None = None,
        updated_at: datetime or None = None
    ):
        self.id = id
        self.config_ui_schema = config_ui_schema
        self.payment_gateway = payment_gateway
        self.name = name
        self.created_at = created_at
        self.updated_at = updated_at

    @classmethod
    def create_new(
        cls,
        config_ui_schema: dict,
        payment_gateway: str,
        name: str
    ):
        return PaymentGateway(
            id=None,
            config_ui_schema=config_ui_schema,
            payment_gateway=payment_gateway,
            name=name
        )

    @classmethod
    def placeholder(
        cls,
        id
    ):
        return cls(
            id=id,
            config_ui_schema={},
            payment_gateway=None,
            name=None
        )

    def diff(self, other):
        differences = {}
        fields = (
            'config_ui_schema', 'payment_gateway', 'name'
        )
        for field in fields:
            if getattr(self, field) != getattr(other, field):
                differences[field] = getattr(self, field)
        return differences


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


class MerchantAccount:
    def __init__(
        self,
        id: int,
        status: str,
        payment_gateway: str or None,
        config: dict,
        label: str,
        fulfilment_points: [FulfilmentPoint] = [],
        created_at: datetime or None = None,
        updated_at: datetime or None = None
    ):
        self.id = id
        self.status = status
        self.payment_gateway = PaymentGateway.placeholder(id=payment_gateway)
        self.config = config
        self.label = label
        self.fulfilment_points = fulfilment_points
        self.created_at = created_at
        self.updated_at = updated_at

    @classmethod
    def create_new(
        cls,
        status: str,
        payment_gateway: str,
        config: dict,
        label: str,
        fulfilment_points: [FulfilmentPoint] = []
    ):
        if isinstance(payment_gateway, (str, int)):
            payment_gateway = PaymentGateway.placeholder(id=payment_gateway)

        return MerchantAccount(
            id=None,
            status=status,
            payment_gateway=payment_gateway,
            config=config,
            label=label,
            fulfilment_points=fulfilment_points
        )

    @classmethod
    def placeholder(
        cls,
        id
    ):
        return cls(
            id=id,
            status=None,
            payment_gateway=None,
            config=None,
            label=None,
            fulfilment_points=[]
        )

    def diff(self, other):
        differences = {}
        fields = (
            'status', 'config', 'label', 'fulfilment_points'
        )
        for field in fields:
            if getattr(self, field) != getattr(other, field):
                differences[field] = getattr(self, field)
        return differences

    @property
    def payment_gateway_id(self):
        return self._payment_gateway.id

    @property
    def payment_gateway(self):
        return self._payment_gateway
