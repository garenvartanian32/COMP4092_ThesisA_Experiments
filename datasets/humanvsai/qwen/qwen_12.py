def delete_handler(Model, name=None, **kwds):

    def handler(type, payload):
        id = payload.get('id')
        if id is None:
            raise ValueError("Payload must contain an 'id' field")
        instance = Model.get(id)
        if instance is None:
            raise ValueError(f'No instance of {Model.__name__} found with id {id}')
        instance.delete()
        return f'Deleted {Model.__name__} with id {id}'
    return handler