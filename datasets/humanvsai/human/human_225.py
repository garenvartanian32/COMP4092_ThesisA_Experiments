def _create_dataset(
            self, group, chunk_size, compression, compression_opts):
        if chunk_size == 'auto':
            chunks = True
        else:
            # if dtype is a variable str, guess representative size is 20 bytes
            per_chunk = (
                nb_per_chunk(20, 1, chunk_size) if self.dtype == np.dtype('O')
                else nb_per_chunk(
                        np.dtype(self.dtype).itemsize, 1, chunk_size))
            chunks = (per_chunk,)
        shape = (0,)
        maxshape = (None,)
        # raise if per_chunk >= 4 Gb, this is requested by h5py
        group.create_dataset(
            self.name, shape, dtype=self.dtype,
            chunks=chunks, maxshape=maxshape, compression=compression,
            compression_opts=compression_opts)