from livestyled.models.app import App
from livestyled.models.fulfilment_point import FulfilmentPoint
from livestyled.models.product import Product, ProductVariant
from livestyled.models.user import User


class OrderItem:
    def __init__(
            self,
            id,
            product_variant,
            fulfilment_point,
            quantity,
            title,
            subtitle,
            image_url,
            price,
            total_price,
            product,
    ):
        self.id = id
        self.quantity = quantity
        self.title = title
        self.subtitle = subtitle
        self.image_url = image_url
        self.price = price
        self.total_price = total_price

        if product_variant:
            if isinstance(product_variant, ProductVariant):
                self.product_variant = product_variant
            elif isinstance(product_variant, dict):
                self.product_variant = ProductVariant(**product_variant)
            elif isinstance(product_variant, int):
                self.product_variant = ProductVariant.placeholder(id=product_variant)
        else:
            self.product_variant = None

        if fulfilment_point:
            if isinstance(fulfilment_point, FulfilmentPoint):
                self.fulfilment_point = fulfilment_point
            elif isinstance(fulfilment_point, dict):
                self.fulfilment_point = FulfilmentPoint(**fulfilment_point)
            elif isinstance(fulfilment_point, int):
                self.fulfilment_point = FulfilmentPoint.placeholder(id=fulfilment_point)
        else:
            self.fulfilment_point = None

        if product:
            if isinstance(product, Product):
                self.product = product
            elif isinstance(product, dict):
                self.product = Product(**product)
            elif isinstance(product, int):
                self.product = Product.placeholder(id=product)
        else:
            self.product = None


class Order:
    def __init__(
            self,
            id,
            user,
            status,
            gross_amount,
            discount,
            net_amount,
            order_amount,
            order_number,
            items,
            updated_at,
            created_at,
            app,
            collection_date,
            estimated_at,
            fulfilment_point,
    ):
        self.id = id
        self.status = status
        self.gross_amount = gross_amount
        self.discount = discount
        self.net_amount = net_amount
        self.order_amount = order_amount
        self.updated_at = updated_at
        self.created_at = created_at
        self.order_number = order_number
        self.collection_date = collection_date
        self.estimated_at = estimated_at

        if user:
            if isinstance(user, User):
                self.user = user
            elif isinstance(user, dict):
                self.user = User(**user)
            elif isinstance(user, int):
                self.user = User.placeholder(id=user)
        else:
            self.user = None

        if items:
            self.items = []
            for item in items:
                if isinstance(item, OrderItem):
                    self.items.append(item)
                elif isinstance(item, dict):
                    self.items.append(OrderItem(**item))
        else:
            self.items = None

        if app:
            if isinstance(app, App):
                self.app = app
            elif isinstance(app, dict):
                self.app = App(**app)
        else:
            self.app = None

        if fulfilment_point:
            if isinstance(fulfilment_point, FulfilmentPoint):
                self.fulfilment_point = fulfilment_point
            elif isinstance(fulfilment_point, dict):
                self.fulfilment_point = FulfilmentPoint(**fulfilment_point)
            elif isinstance(fulfilment_point, int):
                self.fulfilment_point = FulfilmentPoint.placeholder(id=fulfilment_point)
        else:
            self.fulfilment_point = None

    @classmethod
    def placeholder(cls, id):
        return cls(
            id,
            user=None,
            status=None,
            gross_amount=None,
            discount=None,
            net_amount=None,
            order_amount=None,
            order_number=None,
            items=None,
            updated_at=None,
            created_at=None,
            app=None,
            collection_date=None,
            estimated_at=None,
            fulfilment_point=None
        )
