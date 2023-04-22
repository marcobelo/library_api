from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine_sync = create_engine("postgresql://user:pass@localhost:5432/library_db")


def make_sync_session() -> sessionmaker:
    return sessionmaker(
        engine_sync,
        expire_on_commit=True,
        autocommit=False,
        autoflush=True,
    )
