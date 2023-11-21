from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.db.database import Base


class Meet(Base):
    __tablename__ = "meets"

    id = Column(Integer, primary_key=True, autoincrement=True)
    match_id = Column(Integer, ForeignKey("proposals.id"))
    status = Column(String)
    created_at = Column(DateTime)

    proposal = relationship("Proposal")
