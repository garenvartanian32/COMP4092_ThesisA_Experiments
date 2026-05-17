def delete(self, async_mode=False, even_attached=False):
    if async_mode:
        self._delete_async(even_attached)
    else:
        self._delete_sync(even_attached)