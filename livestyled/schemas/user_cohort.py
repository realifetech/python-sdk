from marshmallow import EXCLUDE, fields, Schema

from livestyled.models.user_cohort import UserCohort


class UserCohortSchema(Schema):
    class Meta:
        unknown = EXCLUDE
        model = UserCohort
        api_type = 'user_cohorts'
        url = 'user_management/user_cohorts'

    user = fields.String()
    cohort = fields.String()
