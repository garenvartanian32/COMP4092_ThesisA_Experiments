from typing import List
import pandas as pd

def create_sql_table(df: pd.DataFrame, table_name: str) -> List[str]:
    """
    Returns a list of SQL statements that creates a table reflecting the
    structure of a DataFrame with the given table_name. The first entry will
    be a CREATE TABLE statement while the rest will be CREATE INDEX statements.

    Parameters:
    df (pd.DataFrame): The pandas DataFrame whose structure is to be
                       reflected in the SQL table
    table_name (str): Name of the table to be created in SQL

    Returns:
    A list of SQL statements
    """

    columns = [' '.join([col, get_sql_datatype(df[col])]) for col in df.columns]

    # CREATE TABLE statement
    create_table_sql = f"CREATE TABLE {table_name} ({', '.join(columns)});"

    # CREATE INDEX statements
    create_index_sqls = [f"CREATE INDEX idx_{table_name}_{col} ON {table_name} ({col});"
                          for col in df.columns]

    return [create_table_sql] + create_index_sqls


def get_sql_datatype(data: pd.Series) -> str:
    """
    Returns the corresponding SQL data type for the provided pandas series

    Parameters:
    data (pd.Series): Pandas series whose datatype is to be converted to SQL
                      datatype

    Returns:
    SQL datatype string
    """

    if data.dtype == 'object':
        return 'VARCHAR'
    elif data.dtype == 'int64':
        return 'INT'
    elif data.dtype == 'float64':
        return 'FLOAT'
    elif data.dtype == 'bool':
        return 'BOOLEAN'
    else:
        return 'VARCHAR' # default datatype if not covered above
