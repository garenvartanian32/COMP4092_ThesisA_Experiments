from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Collection(Base):
    __tablename__ = 'collections'

    id = Column(Integer, primary_key=True)
    name = Column(String)

    def __init__(self, name):
        self.name = name

    def remove(self):
        engine = create_engine('sqlite:///example.db')  # use your own connection string
        Session = sessionmaker(bind=engine)
        session = Session()

        # delete all records in the collection
        session.query(Record).filter(Record.collection_id == self.id).delete()

        # delete the collection
        session.delete(self)
        session.commit()

        return f"Collection {self.name} and all records in the collection have been deleted."