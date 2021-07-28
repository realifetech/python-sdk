from livestyled.models.ticket_integration import TicketIntegration
from livestyled.models.user import UserEmail


class TicketAuth:
    def __init__(
            self,
            id,
            client_email,
            client_id,
            user_email,
            ticket_integration,
            access_token=None,
            refresh_token=None,
            expire_at=None
    ):
        self.id = id
        self.client_email = client_email
        self.client_id = client_id
        self.access_token = access_token
        self.refresh_token = refresh_token
        self.expire_at = expire_at
        if user_email:
            if isinstance(user_email, UserEmail):
                self.user_email = user_email
            elif isinstance(user_email, dict):
                self.user_email = UserEmail(**user_email)
            elif isinstance(user_email, (str, int)):
                self.user_email = UserEmail.placeholder(user_email)
        else:
            self.user_email = None
        if ticket_integration:
            if isinstance(ticket_integration, TicketIntegration):
                self.ticket_integration = ticket_integration
            elif isinstance(ticket_integration, dict):
                self.ticket_integration = TicketIntegration(**ticket_integration)
            elif isinstance(ticket_integration, (str, int)):
                self.ticket_integration = TicketIntegration.placeholder(ticket_integration)
        else:
            self.ticket_integration = None

    @classmethod
    def placeholder(
            cls,
            id
    ):
        return cls(
            id=id,
            client_id=None,
            client_email=None,
            access_token=None,
            refresh_token=None,
            expire_at=None,
            user_email=None,
            ticket_integration=None
        )

    @classmethod
    def create_new(
            cls,
            client_id,
            client_email,
            user_email,
            ticket_integration,
            access_token=None,
            refresh_token=None,
            expire_at=None
    ):
        return TicketAuth(
            id=None,
            client_id=client_id,
            client_email=client_email,
            access_token=access_token,
            refresh_token=refresh_token,
            expire_at=expire_at,
            user_email=user_email,
            ticket_integration=ticket_integration
        )

    def __repr__(self):
        return '<TicketAuth(id={self.id!r})>'.format(self=self)

    def diff(self, other):
        differences = {}
        fields = (
            'client_id', 'client_email', 'access_token', 'refresh_token', 'expire_at', 'user_email',
            'ticket_integration'
        )
        for field in fields:
            if getattr(self, field) != getattr(other, field):
                differences[field] = getattr(self, field)
        return differences
