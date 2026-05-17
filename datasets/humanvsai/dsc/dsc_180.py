def _split_queries(cls, sql):
    """Splits sql statements at semicolons into discrete queries"""
    return sql.split(';')