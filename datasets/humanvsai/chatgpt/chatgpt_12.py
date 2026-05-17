def delete_handler_factory(Model):
    def delete_handler(action_type, payload):
        if action_type == 'DELETE':
            instance_id = payload.get('id')
            if instance_id:
                Model.delete(instance_id)
        return None
    return delete_handler
