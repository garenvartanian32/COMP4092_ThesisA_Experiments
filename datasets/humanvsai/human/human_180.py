def _split_queries(cls, sql):
        "Splits sql statements at semicolons into discrete queries"
        sql_s = dbt.compat.to_string(sql)
        sql_buf = StringIO(sql_s)
        split_query = snowflake.connector.util_text.split_statements(sql_buf)
        return [part[0] for part in split_query]