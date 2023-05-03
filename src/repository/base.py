from typing import Type

from sqlalchemy import and_, select
from sqlalchemy.ext.asyncio import AsyncSession

from src.config.database import Base
from src.config.logger import logger


class BaseRepository:
    def __init__(self, session: AsyncSession = None, model: Type[Base] = None):
        self.__session = session
        self.__model = model

    def set_session(self, session: AsyncSession):
        self.__session = session

    async def add_one(self, model: Base) -> None:
        self.__session.add(model)
        await self.__session.flush()
        await self.__session.refresh(model)
        logger.info("%s saved in database", model.__class__.__name__)

    async def delete_one(self, filters: list):
        query = select(self.__model).where(and_(*filters))
        result = await self.__session.execute(query)
        to_delete = result.scalars().first()
        to_delete.deleted = True
        logger.info("%s marked as deleted in database", to_delete.__class__.__name__)
