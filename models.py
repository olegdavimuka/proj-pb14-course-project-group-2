from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Text
from sqlalchemy.orm import relationship
from database import Base


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    age = Column(Integer)
    city = Column(String)
    interests = Column(String)
    created_at = Column(DateTime)
    avatar = Column(String)


class Proposal(Base):
    __tablename__ = 'proposals'
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id_1 = Column(Integer, ForeignKey('users.id'))
    user_id_2 = Column(Integer, ForeignKey('users.id'))
    answer_user_1 = Column(String)
    answer_user_2 = Column(String)
    created_at = Column(DateTime)

    user1 = relationship("User", foreign_keys=[user_id_1])
    user2 = relationship("User", foreign_keys=[user_id_2])


class Meet(Base):
    __tablename__ = 'meets'
    id = Column(Integer, primary_key=True, autoincrement=True)
    match_id = Column(Integer, ForeignKey('proposals.id'))
    status = Column(String)
    created_at = Column(DateTime)

    proposal = relationship("Proposal")


class Review(Base):
    __tablename__ = 'reviews'
    id = Column(Integer, primary_key=True, autoincrement=True)
    meet_id = Column(Integer, ForeignKey('meets.id'))
    user_id = Column(Integer, ForeignKey('users.id'))
    comment = Column(Text)
    created_at = Column(DateTime)

    meet = relationship("Meet")
    user = relationship("User")
