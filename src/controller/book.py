from src.config.logger import logger
from src.repository import BookRepository
from src.schema import BookInput, BookModel


class BookController:
    def __init__(self, book_repository: BookRepository = None):
        self.repository = book_repository or BookRepository()

    async def add_book(self, book_input: BookInput) -> BookModel:
        logger.info("BookController.add_book - book_input = %s", book_input.json())
        book_model = await self.repository.add_book(book_input)
        return book_model
