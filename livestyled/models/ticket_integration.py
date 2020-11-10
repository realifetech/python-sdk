class TicketIntegration:
    def __init__(
            self,
            id,
            label,
            name,
            adapter,
            config_payload,
            endpoint_url,
            auth_required,
            module,
            login_request,
            default,
            can_share
    ):
        self.id = id
        self.label = label
        self.name = name
        self.adapter = adapter
        self.config_payload = config_payload
        self.endpoint_url = endpoint_url
        self.auth_required = auth_required
        self.module = module
        self.login_request = login_request
        self.default = default
        self.can_share = can_share

    @classmethod
    def placeholder(
            cls,
            id
    ):
        return cls(
            id=id,
            label=None,
            name=None,
            adapter=None,
            config_payload=None,
            endpoint_url=None,
            auth_required=None,
            module=None,
            login_request=None,
            default=None,
            can_share=None
        )

    @classmethod
    def create_new(
            cls,
            endpoint_url,
            login_request,
            adapter,
            label=None,
            name=None,
            config_payload=None,
            auth_required=None,
            module=None,
            default=None,
            can_share=None
    ):
        ticket_integration = TicketIntegration(
            id=None,
            label=label,
            name=name,
            adapter=adapter,
            config_payload=config_payload,
            endpoint_url=endpoint_url,
            auth_required=auth_required,
            module=module,
            login_request=login_request,
            default=default,
            can_share=can_share
        )
        return ticket_integration

    def __repr__(self):
        return '<TicketIntegration(id={self.id!r})>'.format(self=self)

    def diff(self, other):
        differences = {}
        fields = (
            'label', 'name', 'endpoint_url', 'adapter', 'config_payload',
            'auth_required', 'module', 'login_request', 'default', 'can_share'
        )
        for field in fields:
            if getattr(self, field) != getattr(other, field):
                differences[field] = getattr(self, field)
        return differences
