from contextvars import ContextVar
from typing import Optional

from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session, sessionmaker

from src.config.environemnt import env

Base = declarative_base()
session_holder: ContextVar[Optional[Session]] = ContextVar("session_holder", default=None)

async_engine = create_async_engine(
    env.db_async_url,
    pool_pre_ping=True,  # Check the connection before using it
    echo=True,  # DEBUG
    # sslmode=True,
    # sslrootcert="",
)


async def make_async_session() -> sessionmaker:
    return sessionmaker(
        async_engine,
        class_=AsyncSession,
        autocommit=False,
        autoflush=False,
        expire_on_commit=False,
    )


class SessionHolderContextVarHandle:
    @property
    def session(self) -> Session:
        session = session_holder.get()
        if session is None:
            raise Exception()
        return session


db = SessionHolderContextVarHandle()
