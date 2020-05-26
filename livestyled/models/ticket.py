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
            can_share=False,
            sharer_email=None,
            sharer_id=None,
            redeemed_at=None,
            redeemer_id=None,
            share_code=None,
            redeemer_email=None,
            parent_ticket=None,
            shared_at=None,
            legal_long_text=None,
            legal_short_text=None,
            map_url=None,
            map_image_url=None,
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
        if user_id:
            self._user = User.placeholder(id=user_id)
        else:
            self._user = None
        self.status = status
        self.can_share = can_share
        self.sharer_email = sharer_email
        self.redeemed_at = redeemed_at
        self.share_code = share_code
        self.redeemer_email = redeemer_email
        self.shared_at = shared_at
        if sharer_id:
            self._sharer = User.placeholder(id=sharer_id)
        else:
            self._sharer = None
        if redeemer_id:
            self._redeemer = User.placeholder(id=redeemer_id)
        else:
            self._redeemer = None
        if parent_ticket:
            if isinstance(parent_ticket, dict):
                self._parent_ticket = Ticket(**parent_ticket)
            elif isinstance(parent_ticket, (int, str)):
                self._parent_ticket = Ticket.placeholder(id=int(parent_ticket))
        else:
            self._parent_ticket = None
        self.legal_long_text = legal_long_text
        self.legal_short_text = legal_short_text
        self.map_url = map_url
        self.map_image_url = map_image_url

    @classmethod
    def placeholder(
            cls,
            id
    ):
        return cls(
            id=id,
            external_ticket_id=None,
            seat=None,
            qr_code_url=None,
            title=None,
            external_event_id=None,
            barcode=None,
            sector_name=None,
            venue_name=None,
            venue_room=None,
            client_name=None,
            premium=None,
            client_email=None,
            price=None,
            share_link=None,
            external_customer_ref=None,
            entrance=None,
            section=None,
            row=None,
            price_code=None,
            created_at=None,
            updated_at=None,
            user_id=None,
            status=None,
            session_date=None,
            can_share=False,
            sharer_email=None,
            sharer_id=None,
            redeemed_at=None,
            redeemer_id=None,
            share_code=None,
            redeemer_email=None,
            parent_ticket=None,
            shared_at=None,
            legal_long_text=None,
            legal_short_text=None,
            map_url=None,
            map_image_url=None,
        )

    @classmethod
    def create_new(
            cls,
            user: User or str or int,
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
            status=None,
            can_share=False,
            sharer_email=None,
            sharer: User or str or int or None = None,
            redeemed_at=None,
            redeemer: User or str or int or None = None,
            share_code=None,
            redeemer_email=None,
            parent_ticket=None,
            shared_at=None,
            legal_long_text=None,
            legal_short_text=None,
            map_url=None,
            map_image_url=None,
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
            status=status,
            can_share=can_share,
            sharer_email=sharer_email,
            sharer_id=None,
            redeemed_at=redeemed_at,
            redeemer_id=None,
            share_code=share_code,
            redeemer_email=redeemer_email,
            parent_ticket=None,
            shared_at=shared_at,
            legal_long_text=legal_long_text,
            legal_short_text=legal_short_text,
            map_url=map_url,
            map_image_url=map_image_url,
        )
        if isinstance(user, (str, int)):
            user = User.placeholder(id=user)
        ticket._user = user
        if isinstance(sharer, (str or int)):
            sharer = User.placeholder(id=sharer)
        ticket._sharer = sharer
        if isinstance(redeemer, (str or int)):
            redeemer = User.placeholder(id=redeemer)
        ticket._redeemer = redeemer
        if isinstance(parent_ticket, (str or int)):
            parent_ticket = Ticket.placeholder(id=parent_ticket)
        ticket._parent_ticket = parent_ticket
        return ticket

    @property
    def user_id(self):
        if self._user:
            return self._user.id
        else:
            return None

    @property
    def user(self):
        return self._user

    @property
    def redeemer_id(self):
        if self._redeemer:
            return self._redeemer.id
        else:
            return None

    @property
    def redeemer(self):
        return self._redeemer

    @property
    def sharer_id(self):
        if self._sharer:
            return self._sharer.id
        else:
            return None

    @property
    def sharer(self):
        return self._sharer

    @property
    def parent_ticket(self):
        return self._parent_ticket

    def __repr__(self):
        return '<Ticket(id={self.id!r})>'.format(self=self)

    def diff(self, other):
        differences = {}
        fields = (
            'external_ticket_id', 'seat', 'qr_code_url', 'session_date', 'title', 'external_event_id',
            'barcode', 'sector_name', 'venue_name', 'venue_room', 'client_name', 'premium', 'client_email',
            'price', 'status', 'can_share', 'sharer_email', 'redeemed_at', 'redeemer_id', 'share_code',
            'redeemer_email', 'parent_ticket', 'shared_at', 'legal_long_text', 'legal_short_text', 'map_url',
            'map_image_url'
        )
        for field in fields:
            if getattr(self, field) != getattr(other, field):
                differences[field] = getattr(self, field)
        return differences
