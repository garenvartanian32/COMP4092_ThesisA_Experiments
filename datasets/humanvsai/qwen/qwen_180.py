def _split_queries(cls, sql):
    queries = sql.split(';')
    queries = [query.strip() for query in queries if query.strip()]
    return queries

def _execute_queries(cls, connection, queries):
    """Executes a list of SQL queries on a given database connection"""
    for query in queries:
        with connection.cursor() as cursor:
            cursor.execute(query)
            connection.commit()

def execute_sql(cls, connection, sql):
    """Executes a string of SQL statements on a given database connection"""
    queries = cls._split_queries(sql)
    cls._execute_queries(connection, queries)