from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from src.config.environemnt import env

Base = declarative_base()

async_engine = create_async_engine(
    env.db_async_url,
    pool_pre_ping=True,  # Check the connection before using it
    echo=False,  # DEBUG
    # sslmode=True,
    # sslrootcert="",
)


async def get_async_sessionmaker() -> sessionmaker:
    return sessionmaker(
        async_engine,
        class_=AsyncSession,
        autocommit=False,
        autoflush=False,
        expire_on_commit=False,
    )
