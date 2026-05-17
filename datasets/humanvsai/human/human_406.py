def to_dict(self, search_fields=None):
        fields = self._fields
        if search_fields == 'update':
            fields = self._search_for_update_fields
        elif search_fields == 'all':
            fields = self._all_searchable_fields
        elif search_fields == 'exclude':
            # exclude search fields for update actions,
            # but include updateable_search_fields
            fields = [field for field in self._fields
                      if field in self._updateable_search_fields or
                      field not in self._search_for_update_fields]
        return {field: self.field_to_dict(field) for field in fields
                if getattr(self, field, None) is not None}