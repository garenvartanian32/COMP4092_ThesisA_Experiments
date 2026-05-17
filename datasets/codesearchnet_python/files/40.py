def _external_items(self):
        """ Return all partitioned items as iterator """
        assert not self.data
        if any(self.pdata):
            self._spill()
        # disable partitioning and spilling when merge combiners from disk
        self.pdata = []

        try:
            for i in range(self.partitions):
                for v in self._merged_items(i):
                    yield v
                self.data.clear()

                # remove the merged partition
                for j in range(self.spills):
                    path = self._get_spill_dir(j)
                    os.remove(os.path.join(path, str(i)))
        finally:
            self._cleanup()