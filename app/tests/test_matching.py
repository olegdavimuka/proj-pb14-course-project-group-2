import random


sample_users = [
    {"name": "Alice", "interests": ["hiking", "technology"], "city": "Kyiv", "preferred_time": "weekend"},
    {"name": "Bob", "interests": ["movies", "technology"], "city": "Vinnitsya", "preferred_time": "evening"},
    {"name": "Charlie", "interests": ["reading", "art"], "city": "Odessa", "preferred_time": "morning"},
    {"name": "Diana", "interests": ["art", "music"], "city": "Odessa", "preferred_time": "weekend"},
    {"name": "Evan", "interests": ["sports", "technology"], "city": "Lviv", "preferred_time": "evening"},
    {"name": "Fiona", "interests": ["music", "movies"], "city": "Kyiv", "preferred_time": "afternoon"},
    {"name": "George", "interests": ["hiking", "nature"], "city": "Kyiv", "preferred_time": "morning"},
    {"name": "Hannah", "interests": ["art", "reading"], "city": "Kyiv", "preferred_time": "weekend"},
    {"name": "Ian", "interests": ["technology", "reading"], "city": "Lviv", "preferred_time": "evening"},
    {"name": "Julia", "interests": ["movies", "sports"], "city": "Lviv", "preferred_time": "afternoon"}
]


def mock_query_gpt(prompt):
    if "hiking" in prompt:
        return "outdoor activities"
    elif "technology" in prompt:
        return "technology"
    
    return "technology"


class MockSession:
    def query(self, model):
        return sample_users


def find_matches(session):
    users = session.query(None)
    matches = []

    for user in users:
        prompt = f"Find a match for a user interested in {', '.join(user['interests'])} from {user['city']}."
        gpt_suggestion = mock_query_gpt(prompt)

        potential_matches = [
            u for u in users if gpt_suggestion in u['interests'] and u['name'] != user['name']
        ]

        if potential_matches:
            matched_user = random.choice(potential_matches)
            matches.append((user['name'], matched_user['name']))

    return matches


mock_session = MockSession()
matched_users = find_matches(mock_session)

for user1, user2 in matched_users:
    print(f"Match found: {user1} and {user2}")
