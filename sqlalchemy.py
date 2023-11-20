from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


DATABASE_URI = 'postgresql://{user}:{password}@{host}:{port}/{database}'

engine = create_engine(DATABASE_URI)
Session = sessionmaker(bind=engine)
session = Session()
