class SportVenue:
    def __init__(
            self,
            id: int,
            name: str or None,
    ):
        self.id = id
        self.name = name

    @classmethod
    def create_new(
            self,
            name: str,
    ):
        self.id = None
        self.name = name
        return self

    @classmethod
    def placeholder(
            cls,
            id
    ):
        return cls(
            id=id,
            name=None,
        )

    def diff(self, other):
        differences = {}
        for key, value in self.__dict__.items() - other.__dict__.items():
            differences[key] = value
        return differences
