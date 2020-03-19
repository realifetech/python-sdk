from marshmallow import EXCLUDE, fields, Schema

from livestyled.models.ticket import Ticket
from livestyled.schemas.fields import RelatedResourceLinkField
from livestyled.schemas.user import UserSchema


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
