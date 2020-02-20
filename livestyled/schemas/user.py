from marshmallow import EXCLUDE, fields, Schema

from livestyled.schemas.device import DeviceSchema
from livestyled.schemas.fields import RelatedResourceField
from livestyled.models.user import User, UserSSO


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
    device_id = RelatedResourceField(schema=DeviceSchema, data_key='device')


class UserSchema(Schema):
    class Meta:
        unknown = EXCLUDE
        api_type = 'users'
        url = 'v4/users'
        create_url = 'v4/users/register'
        authorise_url = 'v4/users/{}/authorise'
        model = User

    class UserInfo(Schema):
        class Meta:
            unknown = EXCLUDE
        first_name = fields.String(data_key='firstName')
        last_name = fields.String(data_key='lastName')

    id = fields.Int()
    auth_type = fields.String(data_key='authType')
    email = fields.Email()
    password = fields.String()
    device_id = RelatedResourceField(schema=DeviceSchema, data_key='device')
    user_info = fields.Nested(UserInfo, data_key='userInfo')


class UserSSOSchema(Schema):
    class Meta:
        unknown = EXCLUDE
        api_type = 'user_sso',
        url = 'v4/user_ssos'
        model = UserSSO

    id = fields.Int()
    access_token = fields.String(data_key='accessToken')
    refresh_token = fields.String(data_key='refreshToken')
    sub = fields.String()
    expires = fields.DateTime()
    user_id = RelatedResourceField(schema=UserSchema, data_key='user')
