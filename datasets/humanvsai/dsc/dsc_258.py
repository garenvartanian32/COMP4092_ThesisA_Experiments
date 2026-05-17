class MyDatabase:
    @classmethod
    def database_path(cls, project, instance, database):
        """Return a fully-qualified database string."""
        return f"{project}/{instance}/{database}"