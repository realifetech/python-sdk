from livestyled.models.app import Currency
from livestyled.models.event import Event, EventDate
from livestyled.models.ticket_integration import TicketIntegration
from livestyled.models.user import User
from livestyled.models.venue import Venue


class Ticket:
    def __init__(
            self,
            id,
            external_ticket_id,
            external_movement_id,
            seat,
            qr_code_url,
            title,
            legacy_external_event_id,
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
            price_type,
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
            ticket_integration=None,
            venue=None,
            event=None,
            ticket_auth=None,
            event_date=None,
            currency=None,
            external_card_ref=None,
            additional_fields=[],
            printed=True,
            timezone=None,
            ticket_type='ticket'
    ):
        self.id = id
        self.external_ticket_id = external_ticket_id
        self.external_movement_id = external_movement_id
        self.seat = seat
        self.qr_code_url = qr_code_url
        self.session_date = session_date
        self.title = title
        self.legacy_external_event_id = legacy_external_event_id
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
        self.price_type = price_type
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
        self.external_card_ref = external_card_ref
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
        if ticket_integration:
            if isinstance(ticket_integration, dict):
                self._ticket_integration = TicketIntegration(**ticket_integration)
            elif isinstance(ticket_integration, (int, str)):
                self._ticket_integration = TicketIntegration.placeholder(ticket_integration)
            elif isinstance(ticket_integration, TicketIntegration):
                self._ticket_integration = ticket_integration
        else:
            self._ticket_integration = None

        if event:
            if isinstance(event, Event):
                self.event = event
            elif isinstance(event, (int, str)):
                self.event = Event.placeholder(id=event)
            elif isinstance(event, dict):
                self.event = Event(**event)
        else:
            self.event = None

        if event_date:
            if isinstance(event_date, EventDate):
                self.event_date = event_date
            elif isinstance(event_date, (int, str)):
                self.event_date = EventDate.placeholder(id=event_date)
            elif isinstance(event_date, dict):
                self.event_date = EventDate(**event_date)
        else:
            self.event_date = None

        if venue:
            if isinstance(venue, Venue):
                self.venue = venue
            elif isinstance(venue, (int, str)):
                self.venue = Venue.placeholder(id=venue)
            elif isinstance(venue, dict):
                self.venue = Venue(**venue)
        else:
            self.venue = None

        if currency:
            if isinstance(currency, Currency):
                self.currency = currency
            elif isinstance(currency, (int, str)):
                self.currency = Currency.placeholder(id=currency)
            elif isinstance(currency, dict):
                self.currency = Currency(**currency)
        else:
            self.currency = None

        self.additional_fields = additional_fields
        self.printed = printed
        self.timezone = timezone
        self.ticket_type = ticket_type

    @classmethod
    def placeholder(
            cls,
            id
    ):
        return cls(
            id=id,
            external_ticket_id=None,
            external_movement_id=None,
            seat=None,
            qr_code_url=None,
            title=None,
            legacy_external_event_id=None,
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
            price_type=None,
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
            ticket_integration=None,
            venue=None,
            event=None,
            currency=None,
            external_card_ref=None,
            additional_fields=[],
            printed=True,
            timezone=None,
            ticket_type='ticket'
        )

    @classmethod
    def create_new(
            cls,
            user: User or str or int,
            external_ticket_id=None,
            external_movement_id=None,
            seat=None,
            qr_code_url=None,
            session_date=None,
            title=None,
            legacy_external_event_id=None,
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
            price_type=None,
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
            ticket_integration=None,
            venue: Venue or str or int or None = None,
            event: Event or str or int or None = None,
            currency: Currency or None = None,
            external_card_ref=None,
            additional_fields=None,
            printed=True,
            timezone=None,
            ticket_type='ticket'
    ):
        if additional_fields is None:
            additional_fields = []
        ticket = Ticket(
            id=None,
            external_ticket_id=external_ticket_id,
            external_movement_id=external_movement_id,
            seat=seat,
            qr_code_url=qr_code_url,
            session_date=session_date,
            title=title,
            legacy_external_event_id=legacy_external_event_id,
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
            price_type=price_type,
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
            ticket_integration=ticket_integration,
            venue=venue,
            event=event,
            currency=currency,
            external_card_ref=external_card_ref,
            additional_fields=additional_fields,
            printed=printed,
            timezone=timezone,
            ticket_type=ticket_type
        )
        if isinstance(user, (str, int)):
            user = User.placeholder(id=user)
        ticket._user = user
        if isinstance(sharer, (str, int)):
            sharer = User.placeholder(id=sharer)
        ticket._sharer = sharer
        if isinstance(redeemer, (str, int)):
            redeemer = User.placeholder(id=redeemer)
        ticket._redeemer = redeemer
        if isinstance(parent_ticket, (str, int)):
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

    @property
    def ticket_integration(self):
        return self._ticket_integration

    def __repr__(self):
        return '<Ticket(id={self.id!r})>'.format(self=self)

    def diff(self, other):
        differences = {}
        fields = (
            'external_ticket_id', 'seat', 'qr_code_url', 'session_date', 'title', 'legacy_external_event_id',
            'external_event_id', 'barcode', 'sector_name', 'venue_name', 'venue_room', 'client_name', 'premium',
            'client_email', 'price', 'status', 'can_share', 'sharer_email', 'redeemed_at', 'redeemer_id', 'share_code',
            'redeemer_email', 'parent_ticket', 'shared_at', 'legal_long_text', 'legal_short_text', 'map_url',
            'map_image_url', 'ticket_integration', 'entrance', 'row', 'section', 'price_code', 'price_type',
            'external_customer_ref', 'venue', 'event', 'event_date', 'currency', 'external_card_ref',
            'additional_fields', 'printed', 'timezone', 'ticket_type'
        )
        for field in fields:
            if getattr(self, field) != getattr(other, field):
                if field == 'additional_fields' and getattr(other, field):
                    if getattr(self, field):
                        differences[field] = merge_additional_fields(getattr(other, field), getattr(self, field))
                else:
                    differences[field] = getattr(self, field)
        return differences


def merge_additional_fields(current_additional_fields, new_additional_fields):
    current_afs = {item['sort']: item for item in current_additional_fields}
    new_afs = {item['sort']: item for item in new_additional_fields}
    merged = {}

    # get sort values of items in both current/new sets
    all_sort_values = set(current_afs.keys()).union(new_afs.keys())
    for sort_val in all_sort_values:
        if sort_val in new_afs:
            # if there's a new field with this sort value - overwrite existing
            merged[sort_val] = new_afs[sort_val]
        else:
            # otherwise, just keep the existing field
            merged[sort_val] = current_afs[sort_val]
    return list(merged.values())
