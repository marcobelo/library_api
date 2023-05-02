from src.repository.base import BaseRepository
from src.schema import BookInput, BookModel


class BookRepository(BaseRepository):
    async def add_book(self, book_input: BookInput) -> BookModel:
        book_model = BookModel(**book_input.dict())
        await self.add_one(book_model)
        return book_model
