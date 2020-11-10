from marshmallow import EXCLUDE, fields, Schema

from livestyled.models.ticket_auth import TicketAuth
from livestyled.schemas.fields import RelatedResourceField, RelatedResourceLinkField
from livestyled.schemas.ticket_integration import TicketIntegrationSchema
from livestyled.schemas.user import UserEmailSchema


class TicketAuthSchema(Schema):
    class Meta:
        unknown = EXCLUDE
        api_type = 'ticket_auths'
        url = 'ticket_auths'
        model = TicketAuth

    id = fields.Int()
    client_email = fields.String(required=False, missing=None, data_key='clientEmail')
    client_id = fields.String(required=False, missing=None, data_key='clientId')
    access_token = fields.String(required=False, missing=None, data_key='accessToken')
    expire_at = fields.AwareDateTime(data_key='expireAt', allow_none=False, missing=None)
    refresh_token = fields.String(required=False, missing=None, data_key='refreshToken')
    user_email = RelatedResourceField(schema=UserEmailSchema, required=False, missing=None, data_key='userEmail')
    ticket_integration = RelatedResourceLinkField(schema=TicketIntegrationSchema, required=False, missing=None, data_key='ticketIntegration')
