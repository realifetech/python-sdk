class Currency:
    def __init__(
            self,
            id: int or None,
            title: str or None,
            iso_code: str or None,
            sign: str or None,
    ):
        self.id = id
        self.title = title
        self.iso_code = iso_code
        self.sign = sign

    @classmethod
    def create_new(
            self,
            title: str,
            iso_code: str or None,
            sign: str or None,
    ):
        self.id = None
        self.title = title
        self.iso_code = iso_code
        self.sign = sign
        return self

    @classmethod
    def placeholder(
            cls,
            id
    ):
        return cls(
            id=id,
            title=None,
            iso_code=None,
            sign=None,
        )

    def diff(self, other):
        differences = {}
        for key, value in self.__dict__.items() - other.__dict__.items():
            differences[key] = value
        return differences
