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
            return '/{}/{}'.format(self.schema.Meta.url, value)
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
            return '/{}/{}'.format(self.schema.Meta.url, value)
        return None

    def _deserialize(self, value, attr, data, **kwargs):
        if self.many:
            return [self.schema().load(v) for v in value]
        else:
            return self.schema().load(value)
