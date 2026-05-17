def remove(self, key):
        encodedKey = json.dumps(key)
        sql = 'DELETE FROM ' + self.table + ' WHERE name = %s'
        with self.connect() as conn:
            with doTransaction(conn):
                return executeSQL(conn, sql, args=[encodedKey])