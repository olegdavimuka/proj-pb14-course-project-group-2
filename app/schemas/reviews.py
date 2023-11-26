from datetime import datetime

from pydantic import BaseModel


class Review(BaseModel):
    id: int
    meet_id: int
    user_id: int
    comment: str
    created_at: datetime
