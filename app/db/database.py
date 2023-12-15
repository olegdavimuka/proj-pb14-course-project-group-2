import configparser

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


Base = declarative_base()

# from datetime import datetime


# from app.models.user import User


def connect_to_database():
    config = configparser.ConfigParser()
    config.read("config.ini")

    db_config = config["postgresql"]

    DATABASE_URI = f"postgresql+psycopg2://{db_config['user']}:{db_config['password']}@{db_config['host']}:{db_config['port']}/{db_config['database']}"

    engine = create_engine(DATABASE_URI)

    Session = sessionmaker(bind=engine)
    session = Session()
    return session


# def add_user(user_data):
#     new_user = User(
#         name=user_data["reg_name"],
#         age=user_data["reg_age"],
#         city=user_data["reg_city"],
#         interests=user_data["reg_interests"],
#         created_at=datetime.now(),
#         occupation=user_data["reg_occupation"],
#     )
#     session.add(new_user)
#     session.commit()
