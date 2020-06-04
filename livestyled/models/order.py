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
        else:
            self.product_variant = None

        if fulfilment_point:
            if isinstance(fulfilment_point, FulfilmentPoint):
                self.fulfilment_point = fulfilment_point
            elif isinstance(fulfilment_point, dict):
                self.fulfilment_point = FulfilmentPoint(**fulfilment_point)
        else:
            self.fulfilment_point = None

        if product:
            if isinstance(product, Product):
                self.product = product
            elif isinstance(product, dict):
                self.product = Product(**product)
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
            created_at
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

        if user:
            if isinstance(user, User):
                self.user = user
            elif isinstance(user, dict):
                self.user = User(**user)
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
