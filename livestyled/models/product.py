from typing import List

from livestyled.models.fulfilment_point import FulfilmentPoint


class ProductVariant:
    def __init__(
            self,
            id,
            price,
            stocks,
            external_id,
            translations,
            product,
    ):
        self.id = id
        self.price = price
        self.stocks = stocks
        self.external_id = external_id
        self.translations = translations
        if product:
            if isinstance(product, Product):
                self.product = product
            elif isinstance(product, int):
                self.product = Product.placeholder(id=product)
            elif isinstance(product, dict):
                self.product = Product(**product)
        else:
            self.product = None

    @classmethod
    def placeholder(cls, id):
        return cls(
            id,
            price=None,
            stocks=None,
            external_id=None,
            translations=None,
            product=None
        )

    @classmethod
    def create_new(
            cls,
            external_id,
            price,
            product: 'Product',
            translations,
            stocks
    ):
        product_variant = ProductVariant(
            id=None,
            external_id=external_id,
            price=price,
            translations=translations,
            product=product,
            stocks=stocks
        )

        return product_variant

    def diff(self, other):
        differences = {}
        fields = (
            'external_id', 'price', 'translations', 'product'
        )
        for field in fields:
            if getattr(self, field) != getattr(other, field):
                differences[field] = getattr(self, field)
        return differences


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


class ProductModifierListTranslation:
    def __init__(
            self,
            id,
            language,
            title,
            created_at,
            updated_at
    ):
        self.id = id
        self.language = language
        self.title = title
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
            position,
            external_id,
            status,
            translations
    ):
        self.id = id
        self.reference = reference
        self.position = position
        self.external_id = external_id
        self.status = status
        self.translations = translations

    @classmethod
    def create_new(
            cls,
            reference,
            position,
            external_id,
            status,
            translations,
    ):
        product_category = ProductCategory(
            id=None,
            reference=reference,
            position=position,
            external_id=external_id,
            status=status,
            translations=translations
        )

        return product_category

    def diff(self, other):
        differences = {}
        fields = (
            'external_id', 'status', 'reference', 'translations', 'position'
        )
        for field in fields:
            if getattr(self, field) != getattr(other, field):
                differences[field] = getattr(self, field)
        return differences


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
                    image['product'] = self
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
                    variant['product'] = self
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

    @classmethod
    def create_new(
            cls,
            external_id,
            status,
            reference,
            categories: List[ProductCategory] or None,
            translations,
            price,
            fulfilment_points: List[FulfilmentPoint] or None,
            core_product_category,
            holding_time: int or None,
            images,
            modifier_lists,
            reconciliation_group,
            variants: List[ProductVariant] or None
    ):
        product = Product(
            id=None,
            status=status,
            reference=reference,
            categories=categories,
            translations=translations,
            external_id=external_id,
            fulfilment_points=fulfilment_points,
            core_product_category=core_product_category,
            holding_time=holding_time,
            images=images,
            modifier_lists=modifier_lists,
            reconciliation_group=reconciliation_group,
            variants=variants,
        )

        return product

    def diff(self, other):
        differences = {}
        fields = (
            'external_id', 'status', 'reference', 'translations', 'categories', 'fulfilment_points',
            'core_product_category', 'holding_time', 'images', 'modifier_lists', 'reconciliation_group',
            'variants'
        )
        for field in fields:
            if getattr(self, field) != getattr(other, field):
                differences[field] = getattr(self, field)
        return differences
