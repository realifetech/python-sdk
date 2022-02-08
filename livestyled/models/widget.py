from datetime import datetime
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

        if variation:
            if isinstance(variation, dict):
                self.variation = WidgetVariation(**variation)
            if isinstance(variation, str):
                self.variation = WidgetVariation.placeholder(id=variation)

    @classmethod
    def create_new(
            cls,
            reference: str,
            content_type: str,
            variation: str or ScreenVariation,
            position: str or None = None,
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
    def __init__(
            self,
            id: int or str,
            fetch_type: str or None,
            widget: str or Widget = None,
            content_ids: List[str] or None = None,
            reference: str or None = None,
            priority: int or None = None,
            created_at: datetime or None = None,
            updated_at: datetime or None = None
    ):
        self.id = id
        self.fetch_type = fetch_type
        self.content_ids = content_ids
        self.reference = reference
        self.priority = priority
        self.created_at = created_at
        self.update_at = updated_at

        if widget:
            if isinstance(widget, (str, int)):
                self.widget = Widget.placeholder(id=widget)
            elif isinstance(widget, Widget):
                self.widget = widget

    @classmethod
    def create_new(
            cls,
            fetch_type: str,
            widget: str or Widget,
            content_ids: List[str] or None,
            reference: str or None,
            priority: int or None = None,
            created_at: datetime or None = None,
            updated_at: datetime or None = None
    ):
        return WidgetVariation(
            id=None,
            fetch_type=fetch_type,
            widget=widget,
            content_ids=content_ids,
            reference=reference,
            priority=priority,
            created_at=created_at,
            updated_at=updated_at
        )

    @classmethod
    def placeholder(cls, id: int or str):
        return WidgetVariation(
            id=id,
            fetch_type=None,
            widget=None,
            content_ids=None,
            reference=None,
            priority=None,
            created_at=None,
            updated_at=None
        )
