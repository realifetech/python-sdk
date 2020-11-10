class News:
    def __init__(
            self,
            id: int or None,
            headline: str or None,
            url: str,
            author: str,
            image_url: str or None,
            title: str or None,
            external_id: str or None,
            media: dict or None,
            published_at,
            updated_at,
    ):
        self.id = id
        self.headline = headline
        self.image_url = image_url
        self.title = title
        self.external_id = external_id
        self.media = media
        self.url = url
        self.author = author
        self.published_at = published_at
        self.updated_at = updated_at

    @classmethod
    def create_new(
            cls,
            external_id: str,
            headline: str,
            image_url: str,
            title: str,
            media: dict or None,
            url: str,
            author: str,
            published_at,
            updated_at,
    ):
        return News(
            id=None,
            headline=headline,
            image_url=image_url,
            title=title,
            media=media,
            external_id=external_id,
            url=url,
            author=author,
            published_at=published_at,
            updated_at=updated_at,
        )

    def diff(self, other):
        differences = {}
        fields = (
            'headline', 'image_url', 'title', 'external_id', 'media', 'url', 'author', 'published_at',
        )
        for field in fields:
            if getattr(self, field) != getattr(other, field):
                differences[field] = getattr(self, field)
        return differences
