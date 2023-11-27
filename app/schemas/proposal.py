from datetime import datetime

from pydantic import BaseModel


class Proposal(BaseModel):
    id: int
    user_id_1: int
    user_id_2: int
    answer_user_1: str
    answer_user_2: str
    created_at: datetime
