from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


user = 'postgres'
passw = '12345678'
host = 'localhost'
port = '5432'
db = 'coins_db'
engine = create_engine(f'postgresql://{user}:{passw}@{host}:{port}/{db}')
session = sessionmaker(bind=engine)()
Base = declarative_base()
