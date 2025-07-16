from typing import Generator
from sqlalchemy.orm import Session
from db.postgresql.session import SessionLocal
from core.settings import settings


def get_db() -> Generator[Session, None, None]:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# def get_mongo_client():
#     uri = settings.MONGODB_URI
#     db_name = settings.MONGODB_DATABASE
#     client = MongoDBClient(uri, db_name)
#     try:
#         yield client
#     finally:
#         client.close()
