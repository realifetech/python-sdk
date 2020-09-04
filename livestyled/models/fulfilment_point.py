from typing import List

from livestyled.models.venue import Venue


class FulfilmentPointCategoryTranslation:
    def __init__(
            self,
            id,
            language,
            title
    ):
        self.id = id
        self.language = language
        self.title = title


class FulfilmentPointTranslation:
    def __init__(
            self,
            language,
            title,
            description,
            collection_note
    ):
        self.language = language
        self.title = title
        self.description = description
        self.collection_note = collection_note


class FulfilmentPointCategory:
    def __init__(
            self,
            id,
            status,
            translations,
    ):
        self.id = id
        self.status = status

        if translations:
            for translation in translations:
                self.translations = []
                if isinstance(translation, FulfilmentPointCategoryTranslation):
                    self.translations.append(translation)
                elif isinstance(translation, dict):
                    self.translations.append(FulfilmentPointCategoryTranslation(**translation))
        else:
            self.translations = []

    @classmethod
    def placeholder(
            cls,
            id
    ):
        return cls(
            id=id,
            status=None,
            translations=None
        )


class FulfilmentPoint:
    def __init__(
            self,
            id,
            status,
            image_url,
            map_image_url,
            lat,
            long,
            type,
            position,
            reference,
            translations,
            categories,
            venue,
            external_id,
    ):
        self.id = id
        self.status = status
        self.image_url = image_url
        self.map_image_url = map_image_url
        self.lat = lat
        self.long = long
        self.type = type
        self.position = position
        self.reference = reference
        self.external_id = external_id

        if translations:
            for translation in translations:
                self.translations = []
                if isinstance(translation, FulfilmentPointTranslation):
                    self.translations.append(translation)
                elif isinstance(translation, dict):
                    self.translations.append(FulfilmentPointTranslation(**translation))
        else:
            self.translations = []

        if categories:
            for category in categories:
                self.categories = []
                if isinstance(category, FulfilmentPointCategory):
                    self.categories.append(category)
                elif isinstance(category, dict):
                    self.categories.append(FulfilmentPointCategory(**category))
                elif isinstance(category, int):
                    self.categories.append(FulfilmentPointCategory.placeholder(id=category))
        else:
            self.categories = []

        if venue:
            if isinstance(venue, Venue):
                self.venue = venue
            elif isinstance(venue, dict):
                self.venue = Venue(**venue)
            elif isinstance(venue, (str, int)):
                self.venue = Venue.placeholder(id=venue)
        else:
            self.venue = None

    @classmethod
    def placeholder(cls, id):
        return cls(
            id,
            status=None,
            image_url=None,
            map_image_url=None,
            lat=None,
            long=None,
            type=None,
            position=None,
            reference=None,
            translations=None,
            categories=None,
            venue=None,
            external_id=None
        )

    @classmethod
    def create_new(
            cls,
            external_id,
            status,
            type: str,
            position: int,
            reference: str,
            image_url: str or None = None,
            map_image_url: str or None = None,
            lat: int or None = None,
            long: int or None = None,
            translations: List or None = None,
            categories: List or None = None,
            venue: str or None = None
    ):
        fulfilment_point = FulfilmentPoint(
            id=None,
            external_id=external_id,
            status=status,
            position=position,
            image_url=image_url,
            map_image_url=map_image_url,
            lat=lat,
            long=long,
            type=type,
            reference=reference,
            translations=translations,
            categories=categories,
            venue=venue
        )
        return fulfilment_point

    def diff(self, other):
        differences = {}
        fields = (
            'external_id', 'type', 'status', 'position', 'reference', 'image_url', 'map_image_url', 'lat', 'long',
            'translations', 'categories', 'venue'
        )
        for field in fields:
            if getattr(self, field) != getattr(other, field):
                differences[field] = getattr(self, field)
        return differences
