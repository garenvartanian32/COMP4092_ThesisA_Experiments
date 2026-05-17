def get_collection(self, **kwargs):
    parent_queryset = self.get_parent_queryset()
    if parent_queryset is None:
        return self.get_queryset()
    else:
        return parent_queryset.filter(**kwargs)