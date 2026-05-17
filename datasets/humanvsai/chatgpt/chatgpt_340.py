def create_storage_container(name, meta_name_values=None, blob_public_access=None, fail_on_exist=False):
    '''
    Creates a storage container

    CLI Example:

    salt-cloud -f create_storage_container my-azure name=mycontainer

    name:
        Name of container to create.

    meta_name_values:
        Optional. A dict with name_value pairs to associate with the
        container as metadata. Example:{'Category':'test'}

    blob_public_access:
        Optional. Possible values include: container, blob

    fail_on_exist:
        Specify whether to throw an exception when the container exists.
    '''
    import azure.batch.models as batchmodels
    container_properties = batchmodels.OutputFileBlobContainerDestination(
        container_url=output_container_sas_url+name,
        path=output_container_name_prefix+name)
    container_client.create_container(
        container_name=name,
        fail_on_exist=fail_on_exist,
        metadata=meta_name_values,
        public_access=blob_public_access)
