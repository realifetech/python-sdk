from marshmallow import fields


class RelatedResourceField(fields.Field):

    def _serialize(self, value, attr, obj, **kwargs):
        return '/{}/{}'.format(self.metadata['schema'].Meta.url, value)

    def _deserialize(self, value, attr, data, **kwargs):
        if 'many' in self.metadata:
            if self.metadata['many']:
                return [int(v.split('/')[-1]) for v in value]
        return int(value.split('/')[-1])
