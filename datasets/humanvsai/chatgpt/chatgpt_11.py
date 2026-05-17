def create_batched_result_record(catalog_brains, batch_size):
    """
    Given a sequence of catalog brains and a batch size,
    create a batched result record by splitting the brains
    into batches of the given size.

    :param catalog_brains: A sequence of catalog brains.
    :param batch_size: The desired size of each batch.
    :returns: A list of batches, where each batch is itself
              a list of catalog brains.
    """
    batches = []
    current_batch = []
    for brain in catalog_brains:
        current_batch.append(brain)
        if len(current_batch) == batch_size:
            batches.append(current_batch)
            current_batch = []
    if current_batch:
        batches.append(current_batch)
    return batches
