from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship


Base = declarative_base()


class Meet(Base):
    __tablename__ = "meets"

    id = Column(Integer, primary_key=True, autoincrement=True)
    match_id = Column(Integer, ForeignKey("proposals.id"))
    status = Column(String)
    created_at = Column(DateTime)

    proposal = relationship("Proposal")
