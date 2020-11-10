class Season:
    def __init__(
            self,
            id: int,
            name: str or None,
            is_current: bool or None,
            external_id: str or None
    ):
        self.id = id
        self.name = name
        self.is_current = is_current
        self.external_id = external_id

    @classmethod
    def create_new(
            self,
            name: str,
            is_current: bool,
            external_id: str or None,
    ):
        self.id = None
        self.name = name
        self.is_current = is_current
        self.external_id = external_id

        return self

    @classmethod
    def placeholder(
            cls,
            id
    ):
        return cls(
            id=id,
            name=None,
            is_current=None,
            external_id=None
        )

    def diff(self, other):
        differences = {}
        fields = (
            'name', 'is_current', 'external_id'
        )
        for field in fields:
            if getattr(self, field) != getattr(other, field):
                differences[field] = getattr(self, field)
        return differences
