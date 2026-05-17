def populate_metadata(model, MetadataClass):
    content_type = ContentType.objects.get_for_model(model)
    for instance in model.objects.all():
        create_metadata_instance(MetadataClass, instance)