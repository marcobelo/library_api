from fastapi import Request
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import sessionmaker


async def async_session(request: Request) -> AsyncSession:
    async_sessionmaker: sessionmaker = request.scope.get("async_sessionmaker")
    async with async_sessionmaker() as session:
        async with session.begin():
            yield session
