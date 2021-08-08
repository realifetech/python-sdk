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


class Currency:
    def __init__(self, id, title, iso_code, sign):
        self.id = id
        self.title = title
        self.iso_code = iso_code
        self.sign = sign

    @classmethod
    def placeholder(
            cls,
            id
    ):
        return cls(
            id=id,
            title=None,
            iso_code=None,
            sign=None
        )
