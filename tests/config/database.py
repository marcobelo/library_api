from mixer import mix_types
from mixer.backend.sqlalchemy import GenFactory, Mixer
from sqlalchemy import create_engine
from sqlalchemy.dialects import postgresql
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


def create_mixer():
    class CustomGenFactory(GenFactory):
        types = dict(GenFactory.types)
        types[postgresql.UUID] = mix_types.UUID

    return Mixer(session=make_sync_session()(), factory=CustomGenFactory)
