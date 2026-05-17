def delete(self, async_mode=False, even_attached=False):
        try:
            return super(UnitySnap, self).delete(async_mode=async_mode)
        except UnityDeleteAttachedSnapError:
            if even_attached:
                log.debug("Force delete the snapshot even if it is attached. "
                          "First detach the snapshot from hosts, then delete "
                          "again.")
                # Currently `detach_from` doesn't process `host` parameter.
                # It always detaches the snapshot from all hosts. So pass in
                # `None` here.
                self.detach_from(None)
                return super(UnitySnap, self).delete(async_mode=async_mode)
            else:
                raise