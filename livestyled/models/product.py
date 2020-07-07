from livestyled.models.fulfilment_point import FulfilmentPoint


class ProductVariant:
    def __init__(
            self,
            id,
            price,
            stocks
    ):
        self.id = id
        self.price = price
        self.stocks = stocks

    @classmethod
    def placeholder(cls, id):
        return cls(
            id,
            price=None,
            stocks=None,
        )


class ProductTranslation:
    def __init__(
            self,
            id,
            language,
            title,
            description,
            created_at,
            updated_at
    ):
        self.id = id
        self.language = language
        self.title = title
        self.description = description
        self.created_at = created_at
        self.updated_at = updated_at


class ProductImage:
    def __init__(
            self,
            id,
            product,
            position,
            created_at,
            updated_at,
            external_id,
            image_url
    ):
        self.id = id
        self.position = position
        self.created_at = created_at
        self.updated_at = updated_at
        self.external_id = external_id
        self.image_url = image_url
        self.product = None
        if product:
            if isinstance(product, Product):
                self.product = product
            elif isinstance(product, dict):
                self.product = Product(**product)
            elif isinstance(product, int):
                self.product = Product.placeholder(id=product)


class ProductCategory:
    def __init__(
            self,
            id,
            reference,
            position
    ):
        self.id = id
        self.reference = reference
        self.position = position


class Product:
    def __init__(
            self,
            id,
            status,
            reference,
            images,
            categories,
            translations,
            modifier_lists,
            external_id,
            holding_time,
            reconciliation_group,
            fulfilment_points,
            variants,
            core_product_category
    ):
        self.id = id
        self.status = status
        self.reference = reference
        self.modifier_lists = modifier_lists
        self.external_id = external_id
        self.holding_time = holding_time
        self.reconciliation_group = reconciliation_group
        self.core_product_category = core_product_category
        if images:
            self.images = []
            for image in images:
                if isinstance(image, ProductImage):
                    self.images.append(image)
                elif isinstance(image, dict):
                    self.images.append(ProductImage(**image))
        else:
            self.images = []

        if categories:
            self.categories = []
            for category in categories:
                if isinstance(category, ProductCategory):
                    self.categories.append(category)
                elif isinstance(category, dict):
                    self.categories.append(ProductCategory(**category))
        else:
            self.categories = []

        if translations:
            self.translations = []
            for translation in translations:
                if isinstance(translation, ProductTranslation):
                    self.translations.append(translation)
                elif isinstance(translation, dict):
                    self.translations.append(ProductTranslation(**translation))
        else:
            self.translations = []

        if fulfilment_points:
            self.fulfilment_points = []
            for fulfilment_point in fulfilment_points:
                if isinstance(fulfilment_point, FulfilmentPoint):
                    self.fulfilment_points.append(fulfilment_point)
                elif isinstance(fulfilment_point, dict):
                    self.fulfilment_points.append(FulfilmentPoint(**fulfilment_point))
                elif isinstance(fulfilment_point, int):
                    self.fulfilment_points.append(FulfilmentPoint.placeholder(id=fulfilment_point))

        if variants:
            self.variants = []
            for variant in variants:
                if isinstance(variant, ProductVariant):
                    self.variants.append(variant)
                elif isinstance(variant, dict):
                    self.variants.append(ProductVariant(**variant))
                elif isinstance(variant, int):
                    self.variants.append(ProductVariant.placeholder(id=variant))

    @classmethod
    def placeholder(
            cls,
            id
    ):
        return cls(
            id=id,
            status=None,
            reference=None,
            images=None,
            categories=None,
            translations=None,
            external_id=None,
            variants=None,
            fulfilment_points=None,
            holding_time=None,
            reconciliation_group=None,
            modifier_lists=None,
            core_product_category=None
        )
