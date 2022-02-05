from datetime import datetime
from typing import Dict, List


class ScreenTranslation:
    def __init__(self, language: str, title: str, **kwargs):
        self.language = language
        self.title = title

        if kwargs:
            for k, v in kwargs.items():
                setattr(self, k, v)


class Screen:
    def __init__(
            self,
            id: int,
            screen_type: str,
            reference: str or None = None,
            translations: List[Dict] or None = None
    ):
        self.id = id
        self.reference = reference
        self.screen_type = screen_type
        self.translations = []

        if translations:
            for translation in translations:
                if isinstance(translation, dict):
                    self.translations.append(ScreenTranslation(**translation))

    @classmethod
    def placeholder(cls, id):
        return cls(
            id,
            screen_type=None,
            reference=None,
            translations=None,
        )

    @classmethod
    def create_new(cls, reference, screen_type, translations):
        return Screen(
            id=None,
            reference=reference,
            screen_type=screen_type,
            translations=translations
        )


class ScreenVariation:
    def __init__(
            self,
            id: int,
            screen: Screen or str,
            priority: int,
            created_at: datetime,
            updated_at: datetime
    ):
        self.id = id
        self.priority = priority
        self.created_at = created_at
        self.updated_at = updated_at

        if screen:
            if isinstance(screen, Screen):
                self.screen = screen
            elif isinstance(screen, Dict):
                self.screen = Screen(**screen)
            else:
                self.screen = Screen.placeholder(id=screen)
