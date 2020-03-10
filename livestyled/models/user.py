from livestyled.models.device import Device


class User:
    def __init__(
            self,
            id: int or None,
            email: str or None,
            auth_type: str or None,
            user_info: dict or None,
            device_id: str or None = None,
            password: str or None = None,
    ):
        self.id = id
        self.email = email
        self.auth_type = auth_type
        self._device = Device.placeholder(id=device_id)
        if not user_info:
            user_info = {}
        self.user_info = user_info
        self.first_name = user_info.get('first_name')
        self.last_name = user_info.get('last_name')
        self.password = password

    @classmethod
    def create_new(
            cls,
            email: str,
            auth_type: str,
            first_name: str,
            last_name: str,
            device: str,
            password: str or None
    ):
        user = User(
            id=None,
            email=email,
            auth_type=auth_type,
            user_info={
                'first_name': first_name,
                'last_name': last_name,
            },
            device_id=None,
            password=password
        )
        user._device = device
        return user

    @classmethod
    def placeholder(
            cls,
            id
    ):
        return cls(
            id=id,
            email=None,
            auth_type=None,
            user_info={},
            device_id=None,
            password=None,
        )

    def diff(self, other):
        differences = {}
        fields = (
            'email', 'auth_type', 'user_info'
        )
        for field in fields:
            if getattr(self, field) != getattr(other, field):
                differences[field] = getattr(self, field)
        return differences

    @property
    def device_id(self):
        return self._device.id

    @property
    def device(self):
        return self._device


class UserSSO:
    def __init__(
            self,
            id,
            user_id,
            access_token,
            refresh_token,
            expires,
            sub
    ):
        self.id = id
        self.access_token = access_token
        self.refresh_token = refresh_token
        self.expires = expires
        self.sub = sub
        self._user = User.placeholder(user_id)

    @classmethod
    def create_new(
            cls,
            user,
            access_token,
            refresh_token,
            expires,
            sub
    ):
        user_sso = UserSSO(
            id=None,
            user_id=None,
            access_token=access_token,
            refresh_token=refresh_token,
            expires=expires,
            sub=sub
        )
        user_sso._user = user
        return user_sso

    def diff(self, other):
        differences = {}
        fields = (
            'access_token', 'refresh_token', 'expires', 'sub', 'user_id'
        )
        for field in fields:
            if getattr(self, field) != getattr(other, field):
                differences[field] = getattr(self, field)
        return differences

    @property
    def user_id(self):
        return self._user.id

    @property
    def user(self):
        return self._user
