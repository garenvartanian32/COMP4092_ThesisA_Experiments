def modify_storage(self, storage, size, title, backup_rule={}):
        res = self._modify_storage(str(storage), size, title, backup_rule)
        return Storage(cloud_manager=self, **res['storage'])