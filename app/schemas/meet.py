from datetime import datetime

from pydantic import BaseModel


class Meet(BaseModel):
    id: int
    match_id: int
    status: str
    created_at: datetime
