from src.config.database import AsyncSessionHolder, Base, db
from src.config.logger import logger


class BaseRepository:
    def __init__(self, database: AsyncSessionHolder = db):
        self.session = database.session

    async def add_one(self, model: Base) -> None:
        self.session.add(model)
        await self.session.flush()
        await self.session.refresh(model)
        logger.info("%s saved in database", model.__class__.__name__)
