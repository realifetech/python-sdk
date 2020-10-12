from datetime import datetime
from typing import Dict, List

from livestyled.models.reality import Reality


class AudienceRealityValueValue:
    def __init__(
            self,
            operator: str,
            value: str
    ):
        self.operator = operator
        self.value = value

    def __str__(self):
        return '{} {}'.format(self.operator, self.value)


class AudienceRealityValue:
    def __init__(
            self,
            reality: Dict,
            values: List[Dict]
    ):
        self.reality = Reality.placeholder(reality)
        self.values = []
        for value in values:
            self.values.append(AudienceRealityValueValue(**value))


class Audience:
    def __init__(
            self,
            id,
            name: str,
            reality_values: List[Dict],
            updated_at: datetime,
            created_at: datetime
    ):
        self.id = id
        self.name = name
        self.created_at = created_at
        self.updated_at = updated_at

        self.reality_values = []
        for reality_value in reality_values:
            self.reality_values.append(AudienceRealityValue(**reality_value))

    @classmethod
    def placeholder(cls, id):
        return cls(
            id,
            name=None,
            reality_values=[],
            updated_at=None,
            created_at=None
        )
