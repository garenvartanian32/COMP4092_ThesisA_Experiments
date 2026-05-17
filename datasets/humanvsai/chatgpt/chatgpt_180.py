def split_sql_statements(sql: str) -> List[str]:
    """
    Splits SQL statements at semicolons into discrete queries.

    Args:
        sql (str): SQL statement(s).

    Returns:
        List[str]: List of discrete SQL queries.
    """
    queries = []
    query = ''
    in_string = False
    for i in range(len(sql)):
        if i == len(sql) - 1:
            query += sql[i]
            queries.append(query)
            continue
        if not in_string:
            if sql[i] == ';':
                queries.append(query)
                query = ''
            else:
                query += sql[i]
                if sql[i] == '\'':
                    in_string = True
        else:
            query += sql[i]
            if sql[i] == '\'' and sql[i - 1] != '\\':
                in_string = False
    return [q.strip() for q in queries if q.strip()]
