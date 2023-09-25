from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker, declarative_base
from os import getenv
from dotenv import load_dotenv
import os
from pathlib import Path

CURR_PATH = Path(__file__)
ENV_PATH = os.path.join(CURR_PATH.parent, "..", "credentials", ".env")
load_dotenv(ENV_PATH, override=True)

URL_DATABASE = getenv("MYSQl_CONNECTION_STRING", "")

engine = create_engine(URL_DATABASE)

meta = MetaData()

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


