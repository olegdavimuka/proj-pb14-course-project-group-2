from datetime import datetime

from pydantic import BaseModel


class User(BaseModel):
    id: int
    name: str
    age: int
    city: str
    interests: str
    created_at: datetime
    avatar: str
