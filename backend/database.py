from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from backend.models import Base
import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def init_db():
    """ Create Database with all tables """
    Base.metadata.create_all(bind=engine)
    print("Database initialised")

def get_db():
    """ Get DB Session """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()