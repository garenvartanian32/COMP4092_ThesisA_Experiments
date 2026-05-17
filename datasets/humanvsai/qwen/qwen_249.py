def modify_storage(self, storage, size, title, backup_rule={}):
    if not isinstance(storage, Storage):
        raise ValueError('Invalid storage object')
    if not isinstance(size, int) or size <= 0:
        raise ValueError('Size must be a positive integer')
    if not isinstance(title, str):
        raise ValueError('Title must be a string')
    if not isinstance(backup_rule, dict):
        raise ValueError('Backup rule must be a dictionary')
    data = {'size': size, 'title': title, 'backup_rule': backup_rule}
    response = self.api_client.put(f'/storages/{storage.id}', data=data)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f'Failed to modify storage: {response.status_code} - {response.text}')