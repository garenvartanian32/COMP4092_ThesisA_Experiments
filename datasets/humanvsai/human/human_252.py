def get_search_index(self, index):
        if not self.yz_wm_index:
            raise NotImplementedError("Search 2.0 administration is not "
                                      "supported for this version")
        url = self.search_index_path(index)
        # Run the request...
        status, headers, body = self._request('GET', url)
        if status == 200:
            return json.loads(bytes_to_str(body))
        else:
            raise RiakError('Error getting Search 2.0 index.')