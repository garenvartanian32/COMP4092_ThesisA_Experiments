def get_collection(self, **kwargs):
    # Assuming self.parent_view is the parent view object
    # and self.parent_view.queryset is the queryset of the parent view
    queryset = self.parent_view.queryset

    # Apply any filters or modifications to the queryset
    # For example, if you want to filter objects that belong to a specific parent object
    parent_object_id = kwargs.get('parent_object_id')
    if parent_object_id:
        queryset = queryset.filter(parent_object_id=parent_object_id)

    return queryset