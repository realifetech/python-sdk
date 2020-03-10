class Cohort:
    def __init__(
            self,
            title,
            external_id
    ):
        self.title = title
        self.external_id = external_id

    def __repr__(self):
        return '<Cohort(title={self.title!r}, external_id={self.external_id!r})>'.format(self=self)
