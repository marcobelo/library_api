from sqlalchemy.orm import sessionmaker

from src.config.database import Base
from src.config.logger import logger


class BaseRepository:
    def __init__(self, session_maker: sessionmaker):
        self.__session_maker = session_maker

    async def add_one(self, model: Base) -> None:
        async with self.__session_maker() as session:
            async with session.begin():
                session.add(model)
                await session.flush()
                await session.refresh(model)
            logger.info("%s saved in database", model.__class__.__name__)
