class Team:
    def __init__(
            self,
            id: int or None,
            name: str or None,
            short_name: str or None,
            light_crest_url: str or None,
            dark_crest_url: str or None,
            external_id: str or None
    ):
        self.id = id
        self.name = name
        self.short_name = short_name
        self.light_crest_url = light_crest_url
        self.dark_crest_url = dark_crest_url
        self.external_id = external_id

    @classmethod
    def placeholder(
            cls,
            id
    ):
        return cls(
            id=id,
            name=None,
            short_name=None,
            light_crest_url=None,
            dark_crest_url=None,
            external_id=None
        )

    @classmethod
    def create_new(
            cls,
            external_id: str,
            name: str,
            short_name: str,
            light_crest_url: str,
            dark_crest_url: str
    ):
        return Team(
            id=None,
            name=name,
            short_name=short_name,
            light_crest_url=light_crest_url,
            dark_crest_url=dark_crest_url,
            external_id=external_id
        )

    def diff(self, other):
        differences = {}
        fields = (
            'name', 'short_name', 'light_crest_url', 'external_id', 'dark_crest_url'
        )
        for field in fields:
            if getattr(self, field) != getattr(other, field):
                differences[field] = getattr(self, field)
        return differences
