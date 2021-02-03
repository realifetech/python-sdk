from livestyled.models.currency import Currency

class App:
    def __init__(
            self,
            id,
            currency,
            email,
            roles,
            password,
            salt,
            username,
            code,
            token,
            name,
            api_keys,
            timezone,
            google_api_key,
            payment_gateway,
            venues,
            sender_email,
            deeplink_namespace,
            merchant_accounts,
            title,
            status,
            cohorts
    ):
        self.id = id
        if currency:
            if isinstance(currency, Currency):
                self.currency = currency
            elif isinstance(currency, dict):
                self.currency = Currency(**currency)
        else:
            self.currency = None
