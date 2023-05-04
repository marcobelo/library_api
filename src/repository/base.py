from typing import Type

from fastapi_pagination import Page
from fastapi_pagination import Params as PaginationParams
from fastapi_pagination.ext.sqlalchemy import paginate
from sqlalchemy import and_, select
from sqlalchemy.ext.asyncio import AsyncSession

from src.config.database import Base
from src.config.exception import NotFoundException
from src.config.logger import logger


class BaseRepository:
    def __init__(self, session: AsyncSession = None, model: Type[Base] = None) -> None:
        self.__session = session
        self.__model = model

    def set_session(self, session: AsyncSession):
        self.__session = session

    async def get_all_paginate(self, params: PaginationParams, filters: list = None) -> Page[Base]:
        query = select(self.__model)
        if filters:
            query = query.where(and_(*filters))
        query = query.order_by(self.__model.id.desc())
        items = await paginate(self.__session, query, params)
        logger.info("Retrieve %s items from database", self.__model.__class__.__name__)
        return items

    async def add_one(self, model: Base) -> None:
        self.__session.add(model)
        await self.__session.flush()
        await self.__session.refresh(model)
        logger.info("%s saved in database", model.__class__.__name__)

    async def delete_one(self, filters: list) -> None:
        class_name = self.__model.__class__.__name__
        query = select(self.__model).where(and_(*filters))
        result = await self.__session.execute(query)
        to_delete = result.scalars().first()
        if not to_delete:
            raise NotFoundException()
        to_delete.deleted = True
        logger.info("%s marked as deleted in database", class_name)
