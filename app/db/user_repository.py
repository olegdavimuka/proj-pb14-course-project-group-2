from datetime import datetime

from models.user import User

from app.db.database import Database


class UserRepository:
    def __init__(self) -> None:
        self.db = Database()

    def add_user(self, user_data):
        new_user = User(
            name=user_data["reg_name"],
            age=user_data["reg_age"],
            city=user_data["reg_city"],
            interests=user_data["reg_interests"],
            created_at=datetime.now(),
            occupation=user_data["reg_occupation"],
        )
        self.db.session.add(new_user)
        self.db.session.commit()
