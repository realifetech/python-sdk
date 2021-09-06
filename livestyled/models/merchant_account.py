from datetime import datetime
from livestyled.models.fulfilment_point import FulfilmentPoint
from livestyled.models.payment_gateway import PaymentGateway

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
        self.payment_gateway = Device.placeholder(id=device_id)
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