from marshmallow import EXCLUDE, fields, Schema

from livestyled.models import Banner, BannerTranslation


class BannerTranslationSchema(Schema):
    class Meta:
        unknown = EXCLUDE
        model = BannerTranslation

    id = fields.Int()
    language = fields.String()
    title = fields.String()
    description = fields.String()
    url = fields.String()
    button_label = fields.String(data_key='buttonLabel')
    image_url = fields.URL(data_key='imageUrl')


class BannerSchema(Schema):
    class Meta:
        unknown = EXCLUDE
        model = Banner
        api_type = 'banner'
        url = 'content_management/banners'

    id = fields.Int()
    name = fields.Str()
    status = fields.String()
    position = fields.String()
    sort_id = fields.Int(data_key='sortId')
    translations = fields.Nested(BannerTranslationSchema, many=True)
    created_at = fields.DateTime(data_key='createdAt')
    updated_at = fields.DateTime(data_key='updatedAt')
