from marshmallow import EXCLUDE, fields, Schema

from livestyled.models.cohort import Cohort


class CohortSchema(Schema):
    class Meta:
        unknown = EXCLUDE
        model = Cohort
        api_type = 'cohorts'
        url = 'cohorts'
        bulk_user_attach_url = 'users/{}/cohorts/bulk-attach'
        bulk_user_detach_url = 'users/{}/cohorts/bulk-detach'

    title = fields.String()
    external_id = fields.String(data_key='externalId', required=False, missing=None)
