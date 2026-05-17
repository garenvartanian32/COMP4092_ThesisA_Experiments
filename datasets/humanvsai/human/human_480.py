def get_collection(self, **kwargs):
        self._query_params.update(kwargs)
        objects = self._parent_queryset()
        if objects is not None:
            return self.Model.filter_objects(
                objects, **self._query_params)
        return self.Model.get_collection(**self._query_params)