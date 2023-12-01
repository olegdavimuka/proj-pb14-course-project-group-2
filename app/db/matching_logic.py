from sqlalchemy.orm import Session
from gpt.api import query_gpt
from models.user import User
import random


def find_matches(session: Session):
    users = session.query(User).all()
    matches = []

    for user in users:
        prompt = f"Find a match for a user interested in {', '.join(user.interests)} from {user.city}."

        gpt_suggestion = query_gpt(prompt)

        potential_matches = [u for u in users if gpt_suggestion in u.interests and u.id != user.id]
        if potential_matches:
            matched_user = random.choice(potential_matches)
            matches.append((user, matched_user))

    return matches


session = Session()
matched_users = find_matches(session)

for user1, user2 in matched_users:
    print(f"Match found: {user1.name} and {user2.name}")
