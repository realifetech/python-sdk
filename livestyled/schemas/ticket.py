from marshmallow import EXCLUDE, fields, Schema
from marshmallow_polyfield import PolyField

from livestyled.models.ticket import Ticket
from livestyled.schemas.fields import RelatedResourceLinkField
from livestyled.schemas.user import UserSchema


def parent_ticket_selector(parent_ticket, ticket):
    if isinstance(parent_ticket, str):
        return RelatedResourceLinkField(schema=Ticket, required=False, missing=None, data_key='parentTicket')
    elif isinstance(parent_ticket, dict):
        return fields.Nested(TicketSchema)


class TicketSchema(Schema):
    class Meta:
        unknown = EXCLUDE
        api_type = 'tickets'
        url = 'v4/tickets'
        model = Ticket

    id = fields.Int()
    external_ticket_id = fields.String(data_key='externalTicketId')
    seat = fields.String(required=False, missing=None)
    qr_code_url = fields.String(data_key='qrCodeUrl', required=False, missing=None)
    session_date = fields.AwareDateTime(data_key='sessionDate', allow_none=False)
    title = fields.String(required=None, missing=False)
    external_event_id = fields.String(data_key='eventUid', required=False, missing=None)
    barcode = fields.String(data_key='barCode', required=False, missing=None)
    sector_name = fields.String(data_key='sectorName', required=False, missing=None)
    venue_name = fields.String(data_key='venueName', required=False, missing=None)
    venue_room = fields.String(data_key='venueRoom', required=False, missing=None)
    client_name = fields.String(data_key='clientName', required=False, missing=None)
    premium = fields.Boolean()
    client_email = fields.String(data_key='clientEmail', required=False, missing=None)
    price = fields.Int(required=False, missing=None)
    share_link = fields.String(data_key='shareLink', required=False, missing=None)
    external_customer_ref = fields.String(data_key='externalCustomerRed', required=False, missing=None)
    entrance = fields.String(required=False, missing=None)
    section = fields.String(required=False, missing=None)
    row = fields.String(required=False, missing=None)
    status = fields.String(required=False, missing=None)
    price_code = fields.String(data_key='priceCode', required=False, missing=None)
    created_at = fields.AwareDateTime(data_key='createdAt', allow_none=False)
    updated_at = fields.AwareDateTime(data_key='updatedAt', allow_none=False)
    user_id = RelatedResourceLinkField(schema=UserSchema, required=False, missing=None, data_key='user')
    can_share = fields.Boolean(data_key='canShare', allow_none=False, required=False, missing=False)
    share_code = fields.String(data_key='shareCode', allow_none=True, required=False, missing=None)
    sharer_email = fields.String(data_key='sharerEmail', allow_none=True, required=False, missing=None)
    redeemer_email = fields.String(data_key='redeemerEmail', allow_none=True, required=False, missing=None)
    redeemed_at = fields.AwareDateTime(data_key='redeemedAt', required=False, missing=None)
    shared_at = fields.AwareDateTime(data_key='sharedAt', required=False, missing=None)
    sharer_id = RelatedResourceLinkField(schema=UserSchema, required=False, missing=None, data_key='sharer')
    redeemer_id = RelatedResourceLinkField(schema=UserSchema, required=False, missing=None, data_key='redeemer')
    parent_ticket = PolyField(
        deserialization_schema_selector=parent_ticket_selector,
        data_key='parentTicket',
        required=False,
        missing=None,
        allow_none=True
    )
    legal_short_text = fields.String(data_key='legalShortText', required=False, allow_none=True, missing=None)
    legal_long_text = fields.String(data_key='legalLongText', required=False, allow_none=True, missing=None)
    map_url = fields.String(data_key='mapUrl', required=False, allow_none=True, missing=None)
    map_image_url = fields.String(data_key='mapImageUrl', required=False, allow_none=True, missing=None)
