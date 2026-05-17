def populate_metadata(model, MetadataClass):
    for instance in model.objects.all():
        (metadata, created) = MetadataClass.objects.get_or_create(instance=instance)
        if created:
            print(f'Created metadata for instance {instance.id}')