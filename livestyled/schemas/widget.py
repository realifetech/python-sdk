from marshmallow import EXCLUDE, fields, Schema

from livestyled.models.widget import Widget, WidgetVariation


class WidgetVariationSchema(Schema):
    class Meta:
        unknown = EXCLUDE
        app_type = 'widget_variations'
        model = WidgetVariation
        url = 'canvas/widget_variations'

    id = fields.Int()
    reference = fields.String()
    widget = fields.String()
    priority = fields.Int()
    fetch_type = fields.String(data_key='fetchType')
    content_ids = fields.List(fields.String, data_key='contentIds')
    created_at = fields.DateTime(data_key='createdAt')
    updated_at = fields.DateTime(data_key='updatedAt')


class WidgetSchema(Schema):
    class Meta:
        unknown = EXCLUDE
        app_type = 'widgets'
        model = Widget
        url = 'canvas/widgets'
        widgets_by_audience = 'canvas/screens/{}/widgets_by_audience'
        widgets_by_screen = 'canvas/screens/{}/widgets'

    id = fields.Int()
    reference = fields.String()
    position = fields.String()
    content_type = fields.String(data_key='contentType')
    variation = fields.Nested(WidgetVariationSchema)
    style = fields.Dict()
    view_all_url = fields.String()
    widget_variation = fields.Dict()
