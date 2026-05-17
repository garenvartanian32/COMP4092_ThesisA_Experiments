from sqlalchemy import create_engine, Table, MetaData
from sqlalchemy.orm import sessionmaker

# Assuming you have a database connection
engine = create_engine('postgresql://user:password@localhost:5432/mydatabase')

# Reflect the tables
metadata = MetaData()
namespace_table = Table('namespace', metadata, autoload_with=engine)

# Start a session
Session = sessionmaker(bind=engine)
session = Session()

def namedb_get_namespace_at(namespace_id, block_number, include_expired=False):
    query = session.query(namespace_table).filter(namespace_table.c.namespace_id == namespace_id, namespace_table.c.block_number <= block_number)

    if not include_expired:
        query = query.filter(namespace_table.c.expired == False)

    return query.all()