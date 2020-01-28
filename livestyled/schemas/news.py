from marshmallow import EXCLUDE, fields, Schema


class NewsSchema(Schema):
    class Meta:
        unknown = EXCLUDE
        api_type = 'news'
        url = 'v4/news'

    class NewsMediaSchema(Schema):
        class Meta:
            unknown = EXCLUDE

        type = fields.String(required=True, allow_none=False)

    id = fields.Int()
    external_id = fields.String(data_key='externalId')
    headline = fields.String(data_key='headline')
    image_url = fields.URL(data_key='imageURL')
    title = fields.String(data_key='title')
    media = fields.Nested(NewsMediaSchema, required=True)
