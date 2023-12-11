from sqlalchemy import Column, DateTime, Integer, String

from app.db.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    age = Column(String)
    city = Column(String)
    interests = Column(String)
    created_at = Column(DateTime)
    occupation = Column(String)
