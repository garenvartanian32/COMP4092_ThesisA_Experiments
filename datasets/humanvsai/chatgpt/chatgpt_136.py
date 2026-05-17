def check_metadata(model, metadata_class):
    instances = model.objects.all()
    for instance in instances:
        metadata, created = metadata_class.objects.get_or_create(instance=instance)
        if created:
            metadata.save()
    return 'Metadata ensured for all instances!'
