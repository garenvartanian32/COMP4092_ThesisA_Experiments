def _cachedSqlType(cls):
        """
        Cache the sqlType() into class, because it's heavy used in `toInternal`.
        """
        if not hasattr(cls, "_cached_sql_type"):
            cls._cached_sql_type = cls.sqlType()
        return cls._cached_sql_type