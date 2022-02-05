from typing import Dict, List

from .screen import ScreenVariation


class Widget:
    def __init__(
            self,
            id: int,
            reference: str or None = None,
            position: int or None = None,
            content_type: str or None = None,
            variation: str or ScreenVariation = None,
            style: dict or None = None,
            view_all_url: str or None = None,
            widget_variation: Dict or None = None
    ):
        self.id = id
        self.reference = reference
        self.position = position
        self.content_type = content_type
        self.variation = variation
        self.style = style
        self.view_all_url = view_all_url
        self.widget_variation = widget_variation

    @classmethod
    def create_new(
            cls,
            reference: str,
            content_type: str,
            variation: str or ScreenVariation,
            position: int = 0,
            view_all_url: str or None = None,
            widget_variation: Dict or None = None
    ):
        return Widget(
            reference=reference,
            position=position,
            variation=variation,
            view_all_url=view_all_url,
            widget_variation=widget_variation,
            content_type=content_type
        )

    @classmethod
    def placeholder(cls, id):
        return cls(
            id=id,
            reference=None,
            position=None,
            content_type=None,
            view_all_url=None,
            widget_variation=None,
            variation=None,
        )


class WidgetVariation:
    def __init__(self):
        pass
