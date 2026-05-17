def get_nested_objects(parent_queryset, nested_object_model, parent_object_id):
    queryset = nested_object_model.objects.filter(parent_relation_id=parent_object_id)
    return queryset.intersection(parent_queryset)