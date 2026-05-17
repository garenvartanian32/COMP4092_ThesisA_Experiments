from tinydb import TinyDB, Query

def search_sample(table, sample):
    """Search for items in `table` that have the same field sub-set values as in `sample`.

    Parameters
    ----------
    table: tinydb.table

    sample: dict
        Sample data

    Returns
    -------
    search_result: list of dict
        List of the items found. The list is empty if no item is found.
    """
    # Create a query object
    q = Query()

    # Create a query that matches all fields in the sample
    query = q.fragment(sample)

    # Search the table
    search_result = table.search(query)

    return search_result