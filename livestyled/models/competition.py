class Competition:
    def __init__(
            self,
            id: int or None,
            name: str or None,
            status: str or None,
            external_id: str or None,
            logo_url: str or None,
            sort_id: int or None,
    ):
        self.id = id
        self.name = name
        self.status = status
        self.logo_url = logo_url
        self.sort_id = sort_id
        self.external_id = external_id

    @classmethod
    def create_new(
            self,
            name: str,
            status: str or None,
            external_id: str or None,
            logo_url: str or None,
            sort_id: int,
    ):
        self.id = None
        self.name = name
        self.status = status
        self.logo_url = logo_url
        self.sort_id = sort_id
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
            status=None,
            external_id=None,
            logo_url=None,
            sort_id=None
        )

    def diff(self, other):
        differences = {}
        for key, value in self.__dict__.items() - other.__dict__.items():
            differences[key] = value
        return differences
