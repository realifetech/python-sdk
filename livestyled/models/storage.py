from datetime import datetime


class Export:
    def __init__(
        self,
        id: int,
        status: str or None = None,
        type: str or None = None,
        filters: dict or None = None,
        url: str or None = None,
        owner: str or None = None,
        created_at: datetime or None = None,
        updated_at: datetime or None = None
    ):
        self.id = id
        self.status = status
        self.type = type
        self.filters = filters
        self.url = url
        self.owner = owner
        self.created_at = created_at
        self.updated_at = updated_at

    @classmethod
    def create_new(cls, status: str, type: str):
        return Export(
            id=None,
            status=status,
            type=type
        )

    @classmethod
    def placeholder(cls, id):
        return cls(id=id)

    def diff(self, other):
        differences = {}
        fields = (
            'status', 'type', 'filters', 'url', 'owner'
        )
        for field in fields:
            if getattr(self, field) != getattr(other, field):
                differences[field] = getattr(self, field)
        return differences
