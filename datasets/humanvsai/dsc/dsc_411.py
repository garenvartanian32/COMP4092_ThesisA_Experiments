from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from your_module import Base, ReplicationDocument

class ReplicationManager:
    def __init__(self):
        engine = create_engine('sqlite:///replication.db')  # Use your database URL here
        Base.metadata.bind = engine
        DBSession = sessionmaker(bind=engine)
        self.session = DBSession()

    def list_replications(self):
        return self.session.query(ReplicationDocument).all()