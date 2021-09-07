from datetime import datetime


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
