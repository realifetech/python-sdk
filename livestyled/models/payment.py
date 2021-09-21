from datetime import datetime

from livestyled.models.fulfilment_point import FulfilmentPoint
from livestyled.models.order import Order
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
        return self.user.id

    @property
    def user(self):
        return self.user


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
        return self.payment_customer.id

    @property
    def payment_customer(self):
        return self.payment_customer


class PaymentIntent:
    def __init__(
        self,
        id: int,
        external_id: str or None,
        payment_customer: str or None,
        status: str,
        amount: int,
        currency: str,
        last_payment_error: str or None,
        live_mode: bool,
        save_payment_source: bool,
        next_action: dict,
        order_type: str,
        order: str or None,
        created_at: datetime or None = None,
        updated_at: datetime or None = None
    ):
        self.id = id
        self.external_id = external_id
        self.payment_customer = PaymentCustomer.placeholder(id=payment_customer)
        self.status = status
        self.amount = amount
        self.currency = currency
        self.last_payment_error = last_payment_error
        self.live_mode = live_mode
        self.save_payment_source = save_payment_source
        self.next_action = next_action
        self.order_type = order_type
        self.order = Order.placeholder(id=order)
        self.created_at = created_at
        self.updated_at = updated_at

    @classmethod
    def create_new(
        cls,
        external_id: str or None,
        payment_customer: str,
        status: str,
        amount: int,
        currency: str,
        last_payment_error: str or None,
        live_mode: bool,
        save_payment_source: bool,
        next_action: dict,
        order_type: str,
        order: str
    ):
        if isinstance(payment_customer, (str, int)):
            payment_customer = PaymentCustomer.placeholder(id=payment_customer)

        if isinstance(order, (str, int)):
            order = Order.placeholder(id=order)

        return PaymentIntent(
            id=None,
            external_id=external_id,
            payment_customer=payment_customer,
            status=status,
            amount=amount,
            currency=currency,
            last_payment_error=last_payment_error,
            live_mode=live_mode,
            save_payment_source=save_payment_source,
            next_action=next_action,
            order_type=order_type,
            order=order
        )

    @classmethod
    def placeholder(
        cls,
        id
    ):
        return cls(
            id=id,
            external_id=None,
            payment_customer=None,
            status=None,
            amount=None,
            currency=None,
            last_payment_error=None,
            live_mode=None,
            save_payment_source=None,
            next_action={},
            order_type=None,
            order=None
        )

    def diff(self, other):
        differences = {}
        fields = (
            'external_id', 'payment_customer', 'status', 'amount', 'currency', 'last_payment_error', 'live_mode', 'save_payment_source', 'next_action', 'order_type', 'order'
        )
        for field in fields:
            if getattr(self, field) != getattr(other, field):
                differences[field] = getattr(self, field)
        return differences

    @property
    def payment_customer_id(self):
        return self.payment_customer.id

    @property
    def payment_customer(self):
        return self.payment_customer

    @property
    def order_id(self):
        return self.order.id

    @property
    def order(self):
        return self.order


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
        return self.payment_gateway.id

    @property
    def payment_gateway(self):
        return self.payment_gateway
