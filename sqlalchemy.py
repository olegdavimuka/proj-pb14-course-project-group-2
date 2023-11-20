from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import configparser


config = configparser.ConfigParser()
config.read('config.ini')

db_config = config['postgresql']

DATABASE_URI = f"postgresql+psycopg2://{db_config['user']}:{db_config['password']}@{db_config['host']}:{db_config['port']}/{db_config['database']}"

engine = create_engine(DATABASE_URI)

Session = sessionmaker(bind=engine)
session = Session()
