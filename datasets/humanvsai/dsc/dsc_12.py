def delete_handler(Model, name=None, **kwds):
    def action_handler(action_type, payload):
        if action_type == 'delete':
            # Assuming payload contains the id of the instance to delete
            instance_id = payload.get('id')
            if instance_id:
                instance = Model.get(instance_id)
                if instance:
                    instance.delete()
                    print(f"Deleted instance {instance_id}")
                else:
                    print(f"Instance {instance_id} not found")
            else:
                print("No instance id provided")
        else:
            print(f"Unsupported action type: {action_type}")

    return action_handler