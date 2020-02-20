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
        for key, value in self.__dict__.items() - other.__dict__.items():
            differences[key] = value
        return differences
