from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from . import settings


db_url = f"postgresql://{settings.DB_USER}:{settings.DB_PASS}@{settings.DB_HOST}:{settings.DB_PORT}/{settings.DB_NAME}"
engine = create_engine(
    db_url,
    future=True,
)

Session = sessionmaker(engine, future=True)
