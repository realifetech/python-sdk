from marshmallow import class_registry, fields
from marshmallow.base import SchemaABC


class RelatedResourceLinkField(fields.Field):

    def __init__(
            self,
            schema=None,
            many=False,
            **kwargs
    ):
        self._schema_arg = schema
        self.many = many
        self.__schema = None
        super(RelatedResourceLinkField, self).__init__(**kwargs)

    @property
    def schema(self):
        if not self.__schema and self._schema_arg:
            if isinstance(self._schema_arg, SchemaABC):
                self.__schema = self._schema_arg
            elif isinstance(self._schema_arg, type) and issubclass(self._schema_arg, SchemaABC):
                self.__schema = self._schema_arg
            elif isinstance(self._schema_arg, str):
                if self._schema_arg == 'self':
                    self.__schema = self.parent.__class__
                else:
                    self.__schema = class_registry.get_class(self._schema_arg)
            else:
                raise ValueError('Nested fields must be passed a Schema, not {0}.'.format(self.nested.__class__))
        return self.__schema

    def _serialize(self, value, attr, obj, **kwargs):
        if value:
            if isinstance(value, (str, int)):
                if getattr(self.schema.Meta, 'include_v4_in_iri', False):
                    return '/v4/{}/{}'.format(self.schema.Meta.url, value)
                return '/{}/{}'.format(self.schema.Meta.url, value)
            else:
                if getattr(self.schema.Meta, 'include_v4_in_iri', False):
                    return '/v4/{}/{}'.format(self.schema.Meta.url, value.id)
                return '/{}/{}'.format(self.schema.Meta.url, value.id)
        return None

    def _deserialize(self, value, attr, data, **kwargs):
        if self.many:
            return [int(v.split('/')[-1]) for v in value]
        elif isinstance(value, dict):
            return int(value['id'])
        return int(value.split('/')[-1])


class RelatedResourceField(fields.Field):

    def __init__(
            self,
            schema=None,
            many=False,
            **kwargs
    ):
        self._schema_arg = schema
        self.many = many
        self.__schema = None
        super(RelatedResourceField, self).__init__(**kwargs)

    @property
    def schema(self):
        if not self.__schema and self._schema_arg:
            if isinstance(self._schema_arg, SchemaABC):
                self.__schema = self._schema_arg
            elif isinstance(self._schema_arg, type) and issubclass(self._schema_arg, SchemaABC):
                self.__schema = self._schema_arg
            elif isinstance(self._schema_arg, str):
                if self._schema_arg == 'self':
                    self.__schema = self.parent.__class__
                else:
                    self.__schema = class_registry.get_class(self._schema_arg)
            else:
                raise ValueError('Nested fields must be passed a Schema, not {0}.'.format(self.nested.__class__))
        return self.__schema

    def _serialize(self, value, attr, obj, **kwargs):
        if value:
            if isinstance(value, (str, int)):
                if getattr(self.schema.Meta, 'include_v4_in_iri', False):
                    return '/v4/{}/{}'.format(self.schema.Meta.url, value)
                return '/{}/{}'.format(self.schema.Meta.url, value)
            elif isinstance(value, list):
                r_value = []
                for v in value:
                    if getattr(self.schema.Meta, 'include_v4_in_iri', False):
                        r_value.append('/v4/{}/{}'.format(self.schema.Meta.url, v.id))
                    r_value.append('/{}/{}'.format(self.schema.Meta.url, v.id))
                return r_value
            else:
                if getattr(self.schema.Meta, 'include_v4_in_iri', False):
                    return '/v4/{}/{}'.format(self.schema.Meta.url, value.id)
                return '/{}/{}'.format(self.schema.Meta.url, value.id)
        else:
            if self.many:
                return []
            else:
                return None

    def _deserialize(self, value, attr, data, **kwargs):
        if self.many:
            deserialized = []
            for v in value:
                if isinstance(v, str):
                    deserialized.append(int(v.split('/')[-1]))
                elif isinstance(v, dict):
                    deserialized.append(self.schema().load(v))
            return deserialized
        else:
            return self.schema().load(value)
