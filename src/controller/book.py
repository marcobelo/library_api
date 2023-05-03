from uuid import UUID

from src.config.logger import logger
from src.repository import BookRepository
from src.schema import BookInput, BookModel


class BookController:
    def __init__(self, book_repository: BookRepository = None):
        self.book_repository = book_repository

    async def add_book(self, book_input: BookInput) -> BookModel:
        logger.info("BookController.add_book - book_input = %s", book_input.json())
        book_model = await self.book_repository.add_book(book_input)
        return book_model

    async def delete_book(self, guid_book: UUID):
        logger.info("BookController.delete_book - guid_book = %s", str(guid_book))
        await self.book_repository.delete_book(guid_book)
