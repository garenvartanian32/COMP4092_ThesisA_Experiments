def listDatabases(self):
        """Returns a list of databases available across all sessions."""
        iter = self._jcatalog.listDatabases().toLocalIterator()
        databases = []
        while iter.hasNext():
            jdb = iter.next()
            databases.append(Database(
                name=jdb.name(),
                description=jdb.description(),
                locationUri=jdb.locationUri()))
        return databases