def _create_table_setup(self):
    create_table_sql = []
    table_name = self.table_name
    columns = self.df.columns
    dtypes = self.df.dtypes
    create_table_sql.append(f'CREATE TABLE {table_name} (')
    column_definitions = []
    for (col, dtype) in zip(columns, dtypes):
        sql_type = self._get_sql_type(dtype)
        column_definitions.append(f'{col} {sql_type}')
    create_table_sql.append(', '.join(column_definitions) + ');')
    for col in columns:
        create_table_sql.append(f'CREATE INDEX idx_{table_name}_{col} ON {table_name} ({col});')
    return create_table_sql