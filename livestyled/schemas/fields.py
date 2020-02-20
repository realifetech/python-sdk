from marshmallow import fields


class RelatedResourceField(fields.Field):

    def _serialize(self, value, attr, obj, **kwargs):
        return '/{}/{}'.format(self.metadata['schema'].Meta.url, value)

    def _deserialize(self, value, attr, data, **kwargs):
        return int(value.split('/')[-1])
