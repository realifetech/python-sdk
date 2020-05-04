from marshmallow import EXCLUDE, fields, Schema

from livestyled.models.news import News


class NewsSchema(Schema):
    class Meta:
        unknown = EXCLUDE
        api_type = 'news'
        url = 'v4/news'
        model = News

    class NewsMediaSchema(Schema):
        class Meta:
            unknown = EXCLUDE

        type = fields.String(required=True, allow_none=False)
        url = fields.String(required=True, allow_none=False)

    id = fields.Int()
    external_id = fields.String(data_key='externalId')
    headline = fields.String(data_key='headline', missing=None)
    image_url = fields.String(data_key='imageUrl', missing=None)
    title = fields.String(data_key='title')
    media = fields.Nested(NewsMediaSchema, missing=None)
    url = fields.String(allow_none=True)
    updated_at = fields.AwareDateTime(data_key='updatedAt', allow_none=False, load_only=True)
    published_at = fields.AwareDateTime(data_key='publishedAt', allow_none=False)
    author = fields.String(required=False, missing=None)
