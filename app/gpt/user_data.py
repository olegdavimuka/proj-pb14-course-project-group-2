import csv


user_data = [
    {"name": "Alice", "interests": "hiking;technology", "city": "Kyiv"},
    {"name": "Bob", "interests": "movies;technology", "city": "Odessa"},
    {"name": "Charlie", "interests": "reading;art", "city": "Lviv"},
    {"name": "Diana", "interests": "art;music", "city": "Odessa"},
    {"name": "Evan", "interests": "sports;technology", "city": "Kyiv"},
    {"name": "Fiona", "interests": "music;movies", "city": "Lviv"},
    {"name": "George", "interests": "hiking;nature", "city": "Kyiv"},
    {"name": "Hannah", "interests": "art;reading", "city": "Lviv"},
    {"name": "Ian", "interests": "technology;reading", "city": "Kyiv"},
    {"name": "Julia", "interests": "movies;sports", "city": "Odessa"}
]

with open('users.csv', 'w') as file:
    writer = csv.DictWriter(file, fieldnames=["name", "interests", "city"])
    writer.writeheader()
    writer.writerows(user_data)
