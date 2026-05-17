def remove_collection(collection):
    """
    A method to remove collection and all records in the collection.

    :param collection: Name of the collection that needs to be removed.
    :return: String with confirmation of deletion.
    """
    # Connect to the database
    client = MongoClient()
    db = client['database_name']

    # Delete the collection
    db[collection].drop()

    # Confirm deletion
    return f'{collection} and all records in the collection have been removed.'
