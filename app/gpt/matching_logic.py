import csv
from collections import defaultdict
from api import query_gpt
import re


def load_users_from_file(file_path):
    users = []
    with open(file_path, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            row['interests'] = row['interests'].split(';')
            users.append(row)
    return users


def group_users_by_city(users):
    city_groups = defaultdict(list)
    for user in users:
        city_groups[user['city']].append(user)
    return city_groups


def create_gpt_prompt_for_city(city, users):
    prompt = (
        f"Create unique networking pairs for a meetup in {city}. "
        "Each person should be paired with exactly one other person from the same city, based on their interests. "
        "Provide the pairings in the format: 'Name1 - Name2'.\n\n"
        "Participants:\n"
    )
    for user in users:
        prompt += f"- {user['name']} (Interests: {', '.join(user['interests'])})\n"
    prompt += "\nSuggested pairings:"
    return prompt


def process_gpt_response(city, gpt_response):
    formatted_pairs = []
    paired_users = set()

    pair_pattern = re.compile(r'\b(\w+)\s*-\s*(\w+)\b')

    for line in gpt_response.split('\n'):
        match = pair_pattern.search(line)
        if match:
            user1, user2 = match.groups()
            if user1 not in paired_users and user2 not in paired_users:
                formatted_pairs.append((city, user1, user2))
                paired_users.update([user1, user2])

    return formatted_pairs


def save_matches_to_file(matches, file_path):
    with open(file_path, 'w', encoding='utf-8', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['City', 'User 1', 'User 2'])
        writer.writerows(matches)


def main():
    users = load_users_from_file('app/gpt/users.csv')
    city_groups = group_users_by_city(users)
    all_matches = []

    for city, users_in_city in city_groups.items():
        prompt = create_gpt_prompt_for_city(city, users_in_city)
        gpt_response = query_gpt(prompt)
        city_pairs = process_gpt_response(city, gpt_response)
        all_matches.extend(city_pairs)

    save_matches_to_file(all_matches, 'app/gpt/matches.csv')


if __name__ == "__main__":
    main()
