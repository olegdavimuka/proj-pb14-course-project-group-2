import csv
from api import query_gpt
import time


def load_users_from_file(file_path):
    users = []
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            row['interests'] = row['interests'].split(';')
            users.append(row)
    return users


def query_gpt_with_retry(prompt, retries=3, delay=30):
    for i in range(retries):
        try:
            return query_gpt(prompt)
        except Exception as e:
            print(f"Attempt {i+1}/{retries}: {e}")
            if i < retries - 1:
                time.sleep(delay)
            else:
                raise


def find_matches(users):
    matches = []
    for user in users:
        prompt = (
            "I am working on a networking application that connects people with similar interests. "
            "The goal is to match users for networking events, meetups, or online discussions "
            "based on their shared or complementary hobbies, activities, and preferences. "
            "Given a user's interests, the application should suggest other interests "
            "that are likely to be compatible or have a meaningful connection for networking purposes. "
            "\n\n"
            f"User's Interests: {', '.join(user['interests'])} from {user['city']}.\n"
            "Suggested Similar Interests:"
        )

        gpt_suggestion = query_gpt_with_retry(prompt)
        suggested_interests = gpt_suggestion.split(', ')

        for potential_match in users:
            if user['city'] == potential_match['city'] and user != potential_match:
                if any(interest in potential_match['interests'] for interest in suggested_interests):
                    matches.append((user['name'], potential_match['name']))

    return matches


def save_matches_to_file(matches, file_path):
    with open(file_path, 'w') as file:
        writer = csv.writer(file)
        writer.writerow(['User 1', 'User 2'])
        for match in matches:
            writer.writerow(match)


users = load_users_from_file('app/gpt/users.csv')

matches = find_matches(users)

save_matches_to_file(matches, 'app/gpt/matches.csv')
