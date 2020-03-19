from livestyled.models.user import User


class Ticket:
    def __init__(
            self,
            id,
            external_ticket_id,
            seat,
            qr_code_url,
            title,
            external_event_id,
            barcode,
            sector_name,
            venue_name,
            venue_room,
            client_name,
            premium,
            client_email,
            price,
            share_link,
            external_customer_ref,
            entrance,
            section,
            row,
            price_code,
            created_at,
            updated_at,
            user_id,
            status,
            session_date=None,
    ):
        self.id = id
        self.external_ticket_id = external_ticket_id
        self.seat = seat
        self.qr_code_url = qr_code_url
        self.session_date = session_date
        self.title = title
        self.external_event_id = external_event_id
        self.barcode = barcode
        self.sector_name = sector_name
        self.venue_name = venue_name
        self.venue_room = venue_room
        self.client_name = client_name
        self.premium = premium
        self.client_email = client_email
        self.price = price
        self.created_at = created_at
        self.updated_at = updated_at
        self.share_link = share_link
        self.external_customer_ref = external_customer_ref
        self.entrance = entrance
        self.section = section
        self.row = row
        self.price_code = price_code
        self._user = User.placeholder(id=user_id)
        self.status = status

    @classmethod
    def create_new(
            cls,
            user: User,
            external_ticket_id=None,
            seat=None,
            qr_code_url=None,
            session_date=None,
            title=None,
            external_event_id=None,
            barcode=None,
            sector_name=None,
            venue_name=None,
            venue_room=None,
            client_name=None,
            premium=False,
            client_email=None,
            price=0,
            row=None,
            section=None,
            share_link=None,
            external_customer_ref=None,
            price_code=None,
            entrance=None,
            status=None
    ):
        ticket = Ticket(
            id=None,
            external_ticket_id=external_ticket_id,
            seat=seat,
            qr_code_url=qr_code_url,
            session_date=session_date,
            title=title,
            external_event_id=external_event_id,
            barcode=barcode,
            sector_name=sector_name,
            venue_name=venue_name,
            venue_room=venue_room,
            client_name=client_name,
            premium=premium,
            client_email=client_email,
            price=price,
            created_at=None,
            updated_at=None,
            share_link=share_link,
            external_customer_ref=external_customer_ref,
            entrance=entrance,
            section=section,
            row=row,
            price_code=price_code,
            user_id=None,
            status=status
        )
        ticket._user = user
        return ticket

    @property
    def user_id(self):
        return self._user.id

    @property
    def user(self):
        return self._user

    def __repr__(self):
        return '<Ticket(id={self.id!r})>'.format(self=self)

    def diff(self, other):
        differences = {}
        fields = (
            'external_ticket_id', 'seat', 'qr_code_url', 'session_date', 'title', 'external_event_id',
            'barcode', 'sector_name', 'venue_name', 'venue_room', 'client_name', 'premium', 'client_email',
            'price', 'status'
        )
        for field in fields:
            if getattr(self, field) != getattr(other, field):
                differences[field] = getattr(self, field)
        return differences
