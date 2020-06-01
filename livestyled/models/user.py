from datetime import datetime
from typing import Dict, List

from livestyled.models.cohort import Cohort
from livestyled.models.device import Device
from livestyled.models.magic_field import MagicField


class UserInfo:
    def __init__(
            self,
            id: int or None = None,
            first_name: str or None = None,
            last_name: str or None = None,
            dob: datetime or None = None,
            gender: str or None = None,
            phone: str or None = None,
    ):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.dob = dob
        self.gender = gender
        self.phone = phone

    def __hash__(self):
        return hash((self.first_name, self.last_name, self.dob, self.gender, self.phone))

    def __eq__(self, other):
        if not isinstance(other, type(self)):
            return NotImplemented
        return all(
            [
                self.first_name == other.first_name,
                self.last_name == other.last_name,
                self.dob == other.dob,
                self.gender == other.gender,
                self.phone == other.phone
            ]
        )


class UserConsent:
    def __init__(
            self,
            id: int or None = None,
            marketing_consent: bool = None,
            analysis_consent: bool = None
    ):
        self.id = id
        self.marketing_consent = marketing_consent
        self.analysis_consent = analysis_consent

    def __hash__(self):
        return hash((self.marketing_consent, self.analysis_consent))

    def __eq__(self, other):
        if not isinstance(other, type(self)):
            return NotImplemented

        return all(
            [
                self.marketing_consent == other.marketing_consent,
                self.analysis_consent == other.analysis_consent
            ]
        )


class UserEmail:
    def __init__(
            self,
            valid: bool,
            email: str
    ):
        self.valid = valid
        self.email = email


class User:
    def __init__(
            self,
            id: int or None,
            email: str or None,
            auth_type: str or None,
            user_info: dict or None,
            device_id: str or None = None,
            password: str or None = None,
            cohorts: List[int] or None = None,
            magic_fields: List[Dict] or None = None,
            user_emails: List[Dict] or None = None,
            user_consent: Dict or None = None,
            devices: List[Dict] or None = None,
    ):
        self.id = id
        self.email = email
        self.auth_type = auth_type
        self._device = Device.placeholder(id=device_id)
        if user_info:
            if isinstance(user_info, dict):
                user_info = UserInfo(**user_info)
            elif isinstance(user_info, UserInfo):
                user_info = user_info
        else:
            user_info = UserInfo(None, None, None, None)
        self.user_info = user_info
        self.first_name = user_info.first_name
        self.last_name = user_info.last_name
        self.password = password
        self.cohorts = []
        if cohorts:
            self.cohorts = [Cohort.placeholder(int(c_id)) for c_id in cohorts]
        if magic_fields:
            self.magic_fields = [MagicField(**m) for m in magic_fields]
        else:
            self.magic_fields = []
        if user_emails:
            self.user_emails = [UserEmail(**u) for u in user_emails]
        else:
            self.user_emails = []
        if user_consent:
            if isinstance(user_consent, UserConsent):
                self.user_consent = user_consent
            elif isinstance(user_consent, dict):
                self.user_consent = UserConsent(**user_consent)
        else:
            self.user_consent = None
        if devices:
            self.devices = [Device(**d) for d in devices]
        else:
            self.devices = []

    @classmethod
    def create_new(
            cls,
            email: str,
            auth_type: str,
            first_name: str,
            last_name: str,
            device: str,
            password: str or None,
            dob: datetime or None = None,
            gender: str or None = None,
            marketing_consent: bool = False,
            analysis_consent: bool = False
    ):
        user = User(
            id=None,
            email=email,
            auth_type=auth_type,
            user_info=UserInfo(first_name=first_name, last_name=last_name, dob=dob, gender=gender),
            device_id=None,
            password=password,
            user_consent=UserConsent(marketing_consent=marketing_consent, analysis_consent=analysis_consent)
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
            user_info=UserInfo(),
            device_id=None,
            password=None,
            user_consent=UserConsent()
        )

    def diff(self, other):
        differences = {}
        fields = (
            'email', 'auth_type', 'user_info',
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
            'access_token', 'refresh_token', 'expires', 'sub', 'user_id',
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
