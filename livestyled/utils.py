schema_map = {}


def _generate_schema_map():
    global schema_map
    from livestyled import schemas
    for schema in schemas.__all__:
        schema_map[schema.Meta.model.__name__] = schema


def create_resource_from_data(resource_model, data):
    if not schema_map:
        _generate_schema_map()
    schema = schema_map[resource_model.__name__]
    d = schema().load(data)
    return resource_model(**d)
