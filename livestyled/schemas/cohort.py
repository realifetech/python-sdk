from marshmallow import EXCLUDE, fields, Schema


class CohortSchema(Schema):
    class Meta:
        unknown = EXCLUDE
        api_type = 'cohorts'
        url = 'v4/cohorts'
        bulk_user_attach_url = 'v4/users/{}/cohorts/bulk-attach'
        bulk_user_detach_url = 'v4/users/{}/cohorts/bulk-detach'

    title = fields.String()
    external_id = fields.String(data_key='externalId')
