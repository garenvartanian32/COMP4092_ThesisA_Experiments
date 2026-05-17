def _collectAsArrow(self):
        """
        Returns all records as a list of ArrowRecordBatches, pyarrow must be installed
        and available on driver and worker Python environments.

        .. note:: Experimental.
        """
        with SCCallSiteSync(self._sc) as css:
            sock_info = self._jdf.collectAsArrowToPython()

        # Collect list of un-ordered batches where last element is a list of correct order indices
        results = list(_load_from_socket(sock_info, ArrowCollectSerializer()))
        batches = results[:-1]
        batch_order = results[-1]

        # Re-order the batch list using the correct order
        return [batches[i] for i in batch_order]