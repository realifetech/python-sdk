from marshmallow import EXCLUDE, fields, Schema

from livestyled.schemas.utils import get_id_from_url


class UserSchema(Schema):
    class Meta:
        unknown = EXCLUDE
        api_type = 'users'
        url = 'v4/users'

    id = fields.Int()
    customer = fields.Dict()  # TODO
    user_info = fields.Dict(data_key='userInfo')  # TODO
    auth_source = fields.String(data_key='authSource')
    token = fields.String()
    auth_type = fields.String(data_key='authType')
    type = fields.String()
    first_name = fields.String(data_key='firstName')
    last_name = fields.String(data_key='lastName')
    status = fields.String()
    roles = fields.List(fields.Inferred)  # TODO
    username = fields.String()
    username_canonical = fields.String(data_key='usernameCanonical')
    salt = fields.String()
    email = fields.Email
    email_canonical = fields.Email(data_key='emailCanonical')
    password = fields.String()
    last_login = fields.AwareDateTime(data_key='lastLogin', allow_none=True)
    account_non_expired = fields.Boolean(data_key='accountNonExpired')
    account_non_locked = fields.Boolean(data_key='accountNonLocked')
    credentials_non_expired = fields.Boolean(data_key='credentialsNonExpired')
    enabled = fields.Boolean()
    super_admin = fields.Boolean(data_key='superAdmin')
    groups = fields.List(fields.Inferred)  # TODO
    group_names = fields.List(fields.Inferred, data_key='groupNames')  # TODO
    app = fields.Function(get_id_from_url)
    devices = fields.List(fields.Inferred)  # TODO
    user_consent = fields.Dict(data_key='userConsent')  # TODO
    user_push_consents = fields.List(fields.Inferred, data_key='userPushConsents')
    tickets = fields.List(fields.Inferred)
    sso_user = fields.Boolean(data_key='SSOUser')
    user_tokens = fields.List(fields.Inferred, data_key='userTokens')
    cohorts = fields.List(fields.Inferred)
    user_emails = fields.List(fields.Inferred, data_key='userEmails')  # TODO
    magic_fields = fields.List(fields.Inferred, data_key='magicFields')  # TODO
    principal_user_email = fields.Dict(data_key='principalUserEmail')  # TODO
    gender = fields.String()
