import configparser

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


config = configparser.ConfigParser()
config.read("config.ini")

db_config = config["postgresql"]

DATABASE_URI = f"postgresql+psycopg2://{db_config['user']}:{db_config['password']}@{db_config['host']}:{db_config['port']}/{db_config['database']}"


class Database:
    def __init__(self):
        self.engine = create_engine(DATABASE_URI)
        Session = sessionmaker(bind=self.engine)
        self.session = Session()


# engine = create_engine(DATABASE_URI)

# Session = sessionmaker(bind=engine)
# session = Session()

# Base = declarative_base()


# def save_user_data(user_data):
#     new_user = User(
#         name=user_data['reg_name'],
#         age=user_data['reg_age'],
#         city=user_data['reg_city'],
#         interests=user_data['reg_interests'],
#         created_at=datetime.now(),
#         avatar=None
#     )
#     session.add(new_user)
#     session.commit()
