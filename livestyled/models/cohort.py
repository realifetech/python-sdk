class Cohort:
    def __init__(
            self,
            title,
            external_id
    ):
        self.id = None
        self.title = title
        self.external_id = external_id

    @classmethod
    def placeholder(
            cls,
            id
    ):
        cohort = cls(
            title=None,
            external_id=None,
        )
        cohort.id = id
        return cohort

    def __repr__(self):
        return '<Cohort(id={self.id!r}, title={self.title!r}, external_id={self.external_id!r})>'.format(self=self)

    def __hash__(self):
        return hash((self.id, self.title, self.external_id))

    def __eq__(self, other):
        if not isinstance(other, type(self)):
            return NotImplemented
        return self.id == other.id and self.title == other.title and self.external_id == other.external_id
