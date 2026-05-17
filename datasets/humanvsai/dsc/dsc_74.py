class SnapshotManager:
    def delete(self, async_mode=False, even_attached=False):
        """Deletes the snapshot.

        :param async_mode: whether to delete the snapshot in async mode.
        :param even_attached: whether to delete the snapshot even it is
            attached to hosts.
        """
        if even_attached:
            print("Deleting snapshot even if it's attached.")
        else:
            print("Deleting snapshot.")

        if async_mode:
            print("Deleting in async mode.")
        else:
            print("Deleting in sync mode.")

# Usage
manager = SnapshotManager()
manager.delete(async_mode=True, even_attached=True)