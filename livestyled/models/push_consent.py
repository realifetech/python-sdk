class PushConsent:
    def __init__(
            self,
            id: int or None,
            type: str or None,
            title: str or None,
            label: str or None,
            sort_id: int or None,
            updated_at,
            created_at,
            translations
    ):
        self.id = id
        self.type = type
        self.title = title
        self.label = label
        self.sort_id = sort_id
        self.updated_at = updated_at
        self.created_at = created_at
        self.translations = translations

    @classmethod
    def create_new(
            cls,
            type,
            title,
            label,
            sort_id,
            updated_at,
            created_at,
            translations
    ):
        return PushConsent(
            id=None,
            type=type,
            label=label,
            title=title,
            sort_id=sort_id,
            updated_at=updated_at,
            created_at=created_at,
            translations=translations
        )

    @classmethod
    def placeholder(
            cls,
            id
    ):
        return cls(
            id=id,
            type=None,
            label=None,
            title=None,
            sort_id=None,
            updated_at=None,
            created_at=None,
            translations=None
        )

    def diff(self, other):
        differences = {}
        fields = (
            'type', 'title', 'sort_id', 'updated_at', 'created_at', 'translations', 'label'
        )
        for field in fields:
            if getattr(self, field) != getattr(other, field):
                differences[field] = getattr(self, field)
        return differences
