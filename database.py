from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy.engine import create_engine
from dotenv import load_dotenv
import os

load_dotenv()

postgres_url = os.getenv("POSTGRESQL_URL")
engine = create_engine(url=postgres_url)
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)
Base = declarative_base()

import models


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
