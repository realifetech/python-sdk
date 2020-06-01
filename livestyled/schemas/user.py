from marshmallow import EXCLUDE, fields, Schema

from livestyled.models.user import User, UserConsent, UserInfo, UserSSO
from livestyled.schemas.cohort import CohortSchema
from livestyled.schemas.device import DeviceSchema
from livestyled.schemas.fields import RelatedResourceField, RelatedResourceLinkField
from livestyled.schemas.magic_field import MagicFieldSchema


class UserCreateSchema(Schema):
    class Meta:
        api_type = 'users'
        url = 'v4/users'
        create_url = 'v4/users/register'
        model = User

    auth_type = fields.String(data_key='authType')
    first_name = fields.String(data_key='firstName')
    last_name = fields.String(data_key='lastName')
    email = fields.Email()
    password = fields.String()
    device_id = RelatedResourceLinkField(schema=DeviceSchema, data_key='device')


class UserInfoSchema(Schema):
    class Meta:
        unknown = EXCLUDE
        api_type = 'user_info'
        url = 'v4/user_infos'
        model = UserInfo

    id = fields.Int()
    first_name = fields.String(data_key='firstName')
    last_name = fields.String(data_key='lastName')
    phone = fields.String(data_key='phone')
    dob = fields.AwareDateTime()
    gender = fields.String()


class UserConsentSchema(Schema):
    class Meta:
        unknown = EXCLUDE
        model = UserConsent

    id = fields.Int()
    marketing_consent = fields.Boolean(data_key='marketingConsent', allow_none=False)
    analysis_consent = fields.Boolean(data_key='analysisConsent', allow_none=False)


class UserSchema(Schema):
    class Meta:
        unknown = EXCLUDE
        api_type = 'users'
        url = 'v4/users'
        create_url = 'v4/users/register'
        authorise_url = 'v4/users/{}/authorise'
        magic_fields_url = 'v4/users/{}/magic_fields'
        model = User

    class UserEmail(Schema):
        class Meta:
            unknown = EXCLUDE
        valid = fields.Boolean()
        email = fields.String()

    id = fields.Int()
    auth_type = fields.String(data_key='authType')
    email = fields.Email()
    password = fields.String()
    device_id = RelatedResourceLinkField(schema=DeviceSchema, data_key='device')
    user_info = fields.Nested(UserInfoSchema, data_key='userInfo')
    cohorts = RelatedResourceLinkField(schema=CohortSchema, many=True)
    magic_fields = RelatedResourceField(schema=MagicFieldSchema, many=True, data_key='magicFields')
    devices = RelatedResourceField(schema=DeviceSchema, many=True, data_key='devices')
    user_emails = fields.Nested(UserEmail, data_key='userEmails', many=True)
    user_consent = RelatedResourceField(schema=UserConsentSchema, data_key='userConsent')


class UserSSOSchema(Schema):
    class Meta:
        unknown = EXCLUDE
        api_type = 'user_sso'
        url = 'v4/user_ssos'
        model = UserSSO

    id = fields.Int()
    access_token = fields.String(data_key='accessToken', missing=None, allow_none=True)
    refresh_token = fields.String(data_key='refreshToken', missing=None, allow_none=True)
    sub = fields.String()
    expires = fields.AwareDateTime(missing=None, allow_none=True)
    user_id = RelatedResourceLinkField(schema=UserSchema, data_key='user')
