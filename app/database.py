from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker 
import psycopg2
from psycopg2.extras import RealDictCursor
import time
from .config import settings
import os
SQLALCHEMY_DATABASE_URL = f'postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}'


DATABASE_HOSTNAME = os.getenv("DATABASE_HOSTNAME", "localhost")
DATABASE_PORT = os.getenv("DATABASE_PORT", "5432")
DATABASE_USERNAME = os.getenv("DATABASE_USERNAME", "postgres")
DATABASE_PASSWORD = os.getenv("DATABASE_PASSWORD", "1234")
DATABASE_NAME = os.getenv("DATABASE_NAME", "fastapi")

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False,autoflush=False,bind=engine)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()    

#Code to connect to the db in case you use local postgres instead of alchemy
# while True:

#     try:
#         conn = psycopg2.connect(host='localhost',database='fastapi', 
#                                 user='postgres',password='1234',cursor_factory=RealDictCursor)
#         cursor = conn.cursor()
#         print("Database connction was succesfull!")
#         break
#     except Exception as error:
#         print("Connection to database failed")
#         print("Error:",error)
#         time.sleep(2)
