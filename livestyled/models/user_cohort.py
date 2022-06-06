class UserCohort:
    def __init__(
            self,
            user,
            cohort
    ):
        self.id = None
        self.user = user
        self.cohort = cohort

    @classmethod
    def placeholder(
            cls,
            id
    ):
        user_cohort = cls(
            user=None,
            cohort=None,
        )
        user_cohort.id = id
        return user_cohort

    def __repr__(self):
        return '<UserCohort(id={self.id!r}, user={self.user!r}, cohort={self.cohort!r})>'.format(self=self)
