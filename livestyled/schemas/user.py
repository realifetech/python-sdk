from marshmallow import EXCLUDE, fields, Schema

from livestyled.models.user import User, UserAlias, UserAliasType, UserConsent, UserEmail, UserInfo, UserSSO
from livestyled.schemas.cohort import CohortSchema
from livestyled.schemas.device import DeviceSchema
from livestyled.schemas.fields import RelatedResourceField, RelatedResourceLinkField
from livestyled.schemas.magic_field import MagicFieldSchema


class UserCreateSchema(Schema):
    class Meta:
        api_type = 'users'
        create_url = 'users/register'
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
        url = 'user_infos'
        model = UserInfo

    id = fields.Int()
    first_name = fields.String(data_key='firstName', missing=None)
    last_name = fields.String(data_key='lastName', missing=None)
    phone = fields.String(data_key='phone', missing=None)
    dob = fields.AwareDateTime(missing=None)
    gender = fields.String(missing=None)


class UserConsentSchema(Schema):
    class Meta:
        unknown = EXCLUDE
        model = UserConsent

    id = fields.Int()
    marketing_consent = fields.Boolean(data_key='marketingConsent', allow_none=False)
    analysis_consent = fields.Boolean(data_key='analysisConsent', allow_none=False)


class UserEmailSchema(Schema):
    class Meta:
        unknown = EXCLUDE
        api_type = 'user_emails'
        url = 'user_emails'
        model = UserEmail

    valid = fields.Boolean()
    email = fields.String()
    id = fields.Int()


class UserAliasTypeSchema(Schema):
    class Meta:
        unknown = EXCLUDE
        api_type = 'user_alias_types'
        url = 'user_management/user_alias_types'
        model = UserAliasType

    user_alias_type = fields.String(data_key='userAliasType', missing=None, allow_none=True)


class UserAliasSchema(Schema):
    class Meta:
        unknown = EXCLUDE
        api_type = 'user_aliases'
        url = 'user_management/user_aliases'
        model = UserAlias

    id = fields.Int()
    user_alias_type = RelatedResourceLinkField(data_key='userAliasType', schema=UserAliasTypeSchema, microservice_aware=True)
    value = fields.String(missing=None)
    updated_at = fields.AwareDateTime(data_key='updatedAt', allow_none=True, missing=None)
    created_at = fields.AwareDateTime(data_key='createdAt', allow_none=True, missing=None)


class UserSchema(Schema):
    class Meta:
        unknown = EXCLUDE
        api_type = 'users'
        url = 'user_management/users'
        create_url = 'users/register'
        authorise_url = 'users/{}/authorise'
        magic_fields_url = 'users/{}/magic_fields'
        model = User

    id = fields.Int()
    auth_type = fields.String(data_key='authType', missing=None)
    email = fields.Email()
    password = fields.String()
    device_id = RelatedResourceLinkField(schema=DeviceSchema, data_key='device')
    user_info = fields.Nested(UserInfoSchema, data_key='userInfo', required=False, missing=None)
    cohorts = RelatedResourceLinkField(schema=CohortSchema, many=True)
    magic_fields = RelatedResourceField(schema=MagicFieldSchema, many=True, data_key='magicFields')
    devices = RelatedResourceField(schema=DeviceSchema, many=True, data_key='devices')
    user_emails = RelatedResourceField(schema=UserEmailSchema, data_key='userEmails', many=True)
    user_consent = RelatedResourceField(schema=UserConsentSchema, data_key='userConsent')
    token = fields.String(missing=None)
    user_aliases = RelatedResourceField(schema=UserAliasSchema, data_key='userAliases', many=True, missing=[])


class UserSSOSchema(Schema):
    class Meta:
        unknown = EXCLUDE
        api_type = 'user_sso'
        url = 'user_ssos'
        model = UserSSO

    id = fields.Int()
    access_token = fields.String(data_key='accessToken', missing=None, allow_none=True)
    refresh_token = fields.String(data_key='refreshToken', missing=None, allow_none=True)
    sub = fields.String()
    expires = fields.AwareDateTime(missing=None, allow_none=True)
    user_id = RelatedResourceLinkField(schema=UserSchema, data_key='user')
