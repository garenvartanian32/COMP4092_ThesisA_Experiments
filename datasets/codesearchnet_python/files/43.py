def sorted(self, iterator, key=None, reverse=False):
        """
        Sort the elements in iterator, do external sort when the memory
        goes above the limit.
        """
        global MemoryBytesSpilled, DiskBytesSpilled
        batch, limit = 100, self._next_limit()
        chunks, current_chunk = [], []
        iterator = iter(iterator)
        while True:
            # pick elements in batch
            chunk = list(itertools.islice(iterator, batch))
            current_chunk.extend(chunk)
            if len(chunk) < batch:
                break

            used_memory = get_used_memory()
            if used_memory > limit:
                # sort them inplace will save memory
                current_chunk.sort(key=key, reverse=reverse)
                path = self._get_path(len(chunks))
                with open(path, 'wb') as f:
                    self.serializer.dump_stream(current_chunk, f)

                def load(f):
                    for v in self.serializer.load_stream(f):
                        yield v
                    # close the file explicit once we consume all the items
                    # to avoid ResourceWarning in Python3
                    f.close()
                chunks.append(load(open(path, 'rb')))
                current_chunk = []
                MemoryBytesSpilled += max(used_memory - get_used_memory(), 0) << 20
                DiskBytesSpilled += os.path.getsize(path)
                os.unlink(path)  # data will be deleted after close

            elif not chunks:
                batch = min(int(batch * 1.5), 10000)

        current_chunk.sort(key=key, reverse=reverse)
        if not chunks:
            return current_chunk

        if current_chunk:
            chunks.append(iter(current_chunk))

        return heapq.merge(chunks, key=key, reverse=reverse)