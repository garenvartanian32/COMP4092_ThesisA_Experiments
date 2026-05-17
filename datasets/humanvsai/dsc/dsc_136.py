def populate_metadata(model, MetadataClass):
    """For a given model and metadata class, ensure there is metadata for every instance."""
    # Get all instances of the model
    instances = model.objects.all()

    # Iterate over each instance
    for instance in instances:
        # Check if metadata exists for this instance
        if not MetadataClass.objects.filter(instance=instance).exists():
            # If not, create metadata for this instance
            MetadataClass.objects.create(instance=instance)