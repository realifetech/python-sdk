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


class ProductModifierList:
    def __init__(
            self,
            id,
            reference,
            status,
            external_id,
            items,
            translations,
            mandatory_select,
            multiple_select
    ):
        self.id = id
        self.reference = reference
        self.items = items
        self.external_id = external_id
        self.status = status
        self.translations = translations
        self.mandatory_select = mandatory_select
        self.multiple_select = multiple_select

    @classmethod
    def create_new(
            cls,
            reference,
            items,
            external_id,
            status,
            translations,
            mandatory_select,
            multiple_select
    ):
        product_modifier_list = ProductModifierList(
            id=None,
            reference=reference,
            items=items,
            external_id=external_id,
            status=status,
            translations=translations,
            mandatory_select=mandatory_select,
            multiple_select=multiple_select
        )

        return product_modifier_list

    @classmethod
    def placeholder(cls, id):
        return cls(
            id,
            reference=None,
            items=None,
            external_id=None,
            translations=None,
            status=None,
            mandatory_select=None,
            multiple_select=None
        )

    def diff(self, other):
        differences = {}
        fields = (
            'external_id', 'status', 'reference', 'translations', 'items', 'mandatory_select', 'multiple_select'
        )
        for field in fields:
            if getattr(self, field) != getattr(other, field):
                differences[field] = getattr(self, field)
        return differences


class ProductModifierItem:
    def __init__(
            self,
            id,
            additional_price,
            translations,
            external_id,
            modifier_list,
    ):
        self.id = id
        self.additional_price = additional_price
        self.external_id = external_id
        self.translations = translations
        self.modifier_list = None
        if modifier_list:
            if isinstance(modifier_list, ProductModifierList):
                self.modifier_list = modifier_list
            elif isinstance(modifier_list, dict):
                self.modifier_list = ProductModifierList(**modifier_list)
            elif isinstance(modifier_list, int):
                self.modifier_list = ProductModifierList.placeholder(id=modifier_list)

    @classmethod
    def create_new(
            cls,
            additional_price,
            external_id,
            translations,
            modifier_list,
    ):
        product_modifier_item = ProductModifierItem(
            id=None,
            additional_price=additional_price,
            external_id=external_id,
            translations=translations,
            modifier_list=modifier_list
        )

        return product_modifier_item

    def diff(self, other):
        differences = {}
        fields = (
            'external_id', 'additional_price', 'translations'
        )
        for field in fields:
            if getattr(self, field) != getattr(other, field):
                differences[field] = getattr(self, field)
        return differences


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
            core_product_category,
    ):
        self.__is_placeholder = False
        self.id = id
        self.status = status
        self.reference = reference
        self.external_id = external_id
        self.holding_time = holding_time
        self.reconciliation_group = reconciliation_group
        self.core_product_category = core_product_category
        if images:
            self.images = images
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
            self.translations = translations
        else:
            self.translations = []

        self.fulfilment_points = []
        if fulfilment_points:
            for fulfilment_point in fulfilment_points:
                if isinstance(fulfilment_point, FulfilmentPoint):
                    self.fulfilment_points.append(fulfilment_point)
                elif isinstance(fulfilment_point, dict):
                    self.fulfilment_points.append(FulfilmentPoint(**fulfilment_point))
                elif isinstance(fulfilment_point, int):
                    self.fulfilment_points.append(FulfilmentPoint.placeholder(id=fulfilment_point))

        self.variants = []
        if variants:
            for variant in variants:
                if isinstance(variant, ProductVariant):
                    self.variants.append(variant)
                elif isinstance(variant, dict):
                    variant['product'] = self
                    self.variants.append(ProductVariant(**variant))
                elif isinstance(variant, int):
                    self.variants.append(ProductVariant.placeholder(id=variant))

        self.modifier_lists = []
        if modifier_lists:
            for modifier_list in modifier_lists:
                if isinstance(modifier_list, ProductModifierList):
                    self.modifier_lists.append(modifier_list)
                elif isinstance(modifier_list, dict):
                    self.modifier_lists.append(ProductModifierList(**modifier_list))
                elif isinstance(modifier_list, int):
                    self.modifier_lists.append(ProductModifierList.placeholder(id=modifier_list))

    @classmethod
    def placeholder(
            cls,
            id
    ):
        product = cls(
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
        product.__is_placeholder = True
        return product

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

    def __eq__(self, other):
        if self.__is_placeholder or other.__is_placeholder:
            return str(self.id) == str(other.id)
        return all(
            [
                self.external_id == other.external_id,
                self.reference == other.reference,
                self.translations == other.translations,
                self.categories == other.categories,
                self.fulfilment_points == other.fulfilment_points,
                self.core_product_category == other.core_product_categories,
                self.holding_time == other.holding_time,
                self.images == other.images,
                self.modifier_lists == other.modifier_lists,
                self.reconciliation_group == other.reconciliation_group,
                self.variants == other.variants,
            ]
        )

    def diff(self, other):
        differences = {}
        fields = (
            'external_id', 'status', 'reference', 'translations',
            'holding_time', 'images', 'reconciliation_group',
            'variants'
        )
        for field in fields:
            if getattr(self, field) != getattr(other, field):
                differences[field] = getattr(self, field)
        related_resource_list_fields = (
            'categories', 'fulfilment_points', 'modifier_lists',
        )
        for field in related_resource_list_fields:
            self_ids = {item.id for item in getattr(self, field)}
            other_ids = {item.id for item in getattr(other, field)}
            if self_ids != other_ids:
                differences[field] = getattr(self, field)
        related_resource_fields = ('core_product_category', )
        for field in related_resource_fields:
            if getattr(getattr(self, field), 'id', None) != getattr(getattr(other, field), 'id', None):
                differences[field] = getattr(self, field)
        return differences
