from datetime import datetime
from typing import Dict


class RealityType:
    def __init__(
            self,
            id,
            name,
            config_json_schema,
            config_ui_schema,
            evaluator,
            watch,
            value_type,
            updated_at,
            created_at,
            combination_key,
    ):
        self.id = id
        self.name = name
        self.config_json_schema = config_json_schema
        self.config_ui_schema = config_ui_schema
        self.evaluator = evaluator
        self.watch = watch
        self.value_type = value_type
        self.updated_at = updated_at
        self.created_at = created_at
        self.combination_key = combination_key

    @classmethod
    def placeholder(cls, id):
        return cls(
            id,
            name=None,
            config_json_schema=None,
            config_ui_schema=None,
            evaluator=None,
            watch=None,
            value_type=None,
            updated_at=None,
            created_at=None,
            combination_key=None,
        )

    def diff(self, other):
        differences = {}
        fields = (
            'name', 'config_json_schema', 'config_ui_schema', 'evaluator', 'watch', 'updated_at', 'created_at', 'combination_key'
        )
        for field in fields:
            if getattr(self, field) != getattr(other, field):
                differences[field] = getattr(self, field)
        return differences


class Reality:
    def __init__(
            self,
            id,
            reality_type: RealityType,
            name: str,
            config: Dict,
            updated_at: datetime,
            created_at: datetime,
            status: str
    ):
        self.id = id
        self.name = name
        self.created_at = created_at
        self.updated_at = updated_at
        self.config = config
        self.status = status

        if reality_type:
            if isinstance(reality_type, RealityType):
                self.reality_type = reality_type
            elif isinstance(reality_type, dict):
                self.reality_type = RealityType(**reality_type)
            elif isinstance(reality_type, int):
                self.reality_type = RealityType.placeholder(id=reality_type)
        else:
            self.reality_type = None

    @classmethod
    def placeholder(cls, id):
        return cls(
            id,
            reality_type=None,
            name=None,
            config={},
            updated_at=None,
            created_at=None,
            status=None,
        )

    def diff(self, other):
        differences = {}
        fields = (
            'reality_type', 'name', 'config', 'status'
        )
        for field in fields:
            if getattr(self, field) != getattr(other, field):
                differences[field] = getattr(self, field)
        return differences
