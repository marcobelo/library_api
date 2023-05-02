from sqlalchemy.ext.asyncio import AsyncSession

from src.config.database import Base
from src.config.logger import logger


class BaseRepository:
    def __init__(self, session: AsyncSession):
        self.__session = session

    async def add_one(self, model: Base) -> None:
        self.__session.add(model)
        await self.__session.flush()
        await self.__session.refresh(model)
        logger.info("%s saved in database", model.__class__.__name__)
