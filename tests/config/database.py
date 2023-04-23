from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from src.config.environemnt import env

engine_sync = create_engine(env.db_sync_url)


def make_sync_session() -> sessionmaker:
    return sessionmaker(
        engine_sync,
        expire_on_commit=True,
        autocommit=False,
        autoflush=True,
    )
