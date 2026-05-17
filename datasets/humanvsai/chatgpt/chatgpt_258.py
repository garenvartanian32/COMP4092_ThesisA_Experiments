def get_database_string(database_name: str, username: str, password: str, host: str, port: int) -> str:
    """
    Returns a fully-qualified database string.

    Args:
        database_name (str): The name of the database.
        username (str): The username for the database.
        password (str): The password for the given username.
        host (str): The database host.
        port (int): The port on which the database is running.

    Returns:
        str: A fully-qualified database string.
    """
    return f'postgresql://{username}:{password}@{host}:{port}/{database_name}'
