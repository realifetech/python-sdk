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
            id,
            language,
            title,
            description,
            collection_note
    ):
        self.id = id
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
        else:
            self.categories = []

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
            categories=None
        )
