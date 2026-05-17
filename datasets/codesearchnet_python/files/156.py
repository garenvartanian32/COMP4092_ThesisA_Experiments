def listTables(self, dbName=None):
        """Returns a list of tables/views in the specified database.

        If no database is specified, the current database is used.
        This includes all temporary views.
        """
        if dbName is None:
            dbName = self.currentDatabase()
        iter = self._jcatalog.listTables(dbName).toLocalIterator()
        tables = []
        while iter.hasNext():
            jtable = iter.next()
            tables.append(Table(
                name=jtable.name(),
                database=jtable.database(),
                description=jtable.description(),
                tableType=jtable.tableType(),
                isTemporary=jtable.isTemporary()))
        return tables