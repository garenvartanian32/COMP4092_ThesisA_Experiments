import sqlite3

def get_column_converters(cursor):
    """
    Returns a mapping of SQLite column names to Converter objects.
    """
    converters = {}
    for i in range(cursor.description):
        col_name = cursor.description[i][0]
        col_type = cursor.description[i][1]
        converters[col_name] = sqlite3.converters[col_type]
    
    return converters
