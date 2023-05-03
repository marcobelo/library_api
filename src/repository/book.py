from uuid import UUID

from sqlalchemy.ext.asyncio import AsyncSession

from src.repository.base import BaseRepository
from src.schema import BookInput, BookModel


class BookRepository(BaseRepository):
    def __init__(self, session: AsyncSession = None):
        super().__init__(session, BookModel)

    async def add_book(self, book_input: BookInput) -> BookModel:
        book_model = BookModel(**book_input.dict())
        await self.add_one(book_model)
        return book_model

    async def delete_book(self, guid_book: UUID):
        filters = [BookModel.guid == guid_book]
        await self.delete_one(filters)
