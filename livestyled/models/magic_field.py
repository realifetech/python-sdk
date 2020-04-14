
class MagicField:
    def __init__(
            self,
            id: int or None,
            key: str,
            value: str,
            user_id: str or int,
    ):
        from livestyled.models.user import User
        self.id = id
        self.key = key
        self.value = value
        self._user = User.placeholder(id=user_id)

    @classmethod
    def create_new(
            cls,
            user,
            key: str,
            value: str,
    ):
        magic_field = MagicField(
            id=None,
            key=key,
            value=value,
            user_id=None,
        )
        from livestyled.models.user import User
        if isinstance(user, (str, int)):
            user = User.placeholder(id=user)
        magic_field._user = user
        return magic_field

    @property
    def user_id(self):
        return self._user.id

    @property
    def user(self):
        return self._user

    def __repr__(self):
        return '<MagicField(id={self.id!r}, key={self.key!r}, value={self.value!r}, user={self.user!r})>'.format(self=self)

    def diff(self, other):
        differences = {}
        fields = (
            'key', 'value'
        )
        for field in fields:
            if getattr(self, field) != getattr(other, field):
                differences[field] = getattr(self, field)
        return differences
