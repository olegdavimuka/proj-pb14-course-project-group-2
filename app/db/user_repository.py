from datetime import datetime

from database import session

from app.models.user import User


def add_user(user_data):
    new_user = User(
        name=user_data["reg_name"],
        age=user_data["reg_age"],
        city=user_data["reg_city"],
        interests=user_data["reg_interests"],
        created_at=datetime.now(),
        occupation=user_data["reg_occupation"],
    )
    session.add(new_user)
    session.commit()
