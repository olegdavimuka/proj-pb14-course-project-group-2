from sqlalchemy import Column, DateTime, Integer, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    age = Column(String)
    city = Column(String)
    interests = Column(String)
    created_at = Column(DateTime)
    occupation = Column(String)
