def search_sample(table, sample):
    from tinydb import Query
    q = Query()
    query = q.fragment(sample)
    search_result = table.search(query)
    return search_result