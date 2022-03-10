from datetime import datetime
from typing import Dict, List, Optional


class BannerTranslation:
    def __init__(
            self,
            id: int or str,
            language: str,
            url: str or None = None,
            title: str or None = None,
            description: str or None = None,
            subtitle: Optional[str] = None,
            button_label: Optional[str] = None,
            image_url: Optional[str] = None
    ):
        self.id = id
        self.language = language
        self.title = title
        self.subtitle = subtitle
        self.description = description
        self.url = url
        self.button_label = button_label
        self.image_url = image_url


class Banner:
    def __init__(
            self,
            id: int or str or None,
            name: str,
            status: str,
            position: str or None,
            sort_id: int,
            created_at: datetime,
            updated_at: datetime,
            translations: List[BannerTranslation] or List[Dict] or None = None,
    ):
        self.id = id
        self.name = name
        self.status = status
        self.position = position
        self.sort_id = sort_id
        self.created_at = created_at
        self.updated_at = updated_at

        if translations:
            self.translations = []

            for item in translations:
                if isinstance(item, Dict):
                    self.translations.append(BannerTranslation(**item))
                elif isinstance(item, BannerTranslation):
                    self.translations.append(item)

    @classmethod
    def create_new(
            cls,
            name: str,
            status: str,
            position: str or None,
            sort_id: int,
            translations: List[BannerTranslation] or None = None,
            created_at: datetime or None = None,
            updated_at: datetime or None = None
    ):
        return Banner(
            id=None,
            name=name,
            status=status,
            position=position,
            sort_id=sort_id,
            translations=translations,
            created_at=created_at,
            updated_at=updated_at
        )

    @classmethod
    def placeholder(cls, id: int or str):
        return cls(
            id=id,
            name=None,
            status=None,
            position=None,
            sort_id=None,
            translations=None,
            created_at=None,
            updated_at=None
        )
