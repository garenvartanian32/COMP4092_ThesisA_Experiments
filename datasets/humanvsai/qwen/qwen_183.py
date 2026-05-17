def namedb_get_namespace_at(cur, namespace_id, block_number, include_expired=False):
    query = '\n    SELECT state, block_number, namespace_id\n    FROM namespace_states\n    WHERE namespace_id = %s\n    AND block_number <= %s\n    ORDER BY block_number DESC\n    LIMIT 1\n    '
    if include_expired:
        query += ' AND expired = False'
    cur.execute(query, (namespace_id, block_number))
    result = cur.fetchone()
    return result