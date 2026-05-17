def get_inventory_temp_file(self, keys=None):
        temp_file = tempfile.NamedTemporaryFile(mode='r+t')
        inventory = self.get_inventory_str(keys)
        LOGGER.debug(
            'Writing inventory to temp file {} \n{}'.format(
                temp_file.name, inventory
            )
        )
        temp_file.write(inventory)
        temp_file.flush()
        temp_file.seek(0)
        yield temp_file
        temp_file.close()