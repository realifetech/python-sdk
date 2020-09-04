from marshmallow import EXCLUDE, fields, Schema

from livestyled.models.ticket_integration import TicketIntegration


class TicketIntegrationSchema(Schema):
    class Meta:
        unknown = EXCLUDE
        api_type = 'ticket_integrations'
        url = 'ticket_integrations'
        model = TicketIntegration
        include_v4_in_iri = True

    id = fields.Int()
    label = fields.String(required=False, missing=None)
    name = fields.String(required=False, missing=None)
    adapter = fields.String(required=False, missing=None)
    endpoint_url = fields.String(required=False, missing=None, data_key='endpointUrl')
    config_payload = fields.String(required=False, missing=None, data_key='configPayload')
    auth_required = fields.Boolean(required=False, missing=None, data_key='authRequired')
    module = fields.String(required=False, missing=None)
    login_request = fields.String(required=False, missing=None, data_key='loginRequest')
    default = fields.Boolean(required=False, missing=None, data_key='default')
    can_share = fields.Boolean(required=False, missing=None, data_key='canShare')
