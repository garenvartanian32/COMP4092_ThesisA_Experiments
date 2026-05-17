def search_sample(table, sample):
    query = _query_sample(sample=sample, operators='__eq__')
    return table.search(query)