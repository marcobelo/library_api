from src.config.database import db
from src.schema import BookInput, BookModel


class BookController:
    @classmethod
    async def add_book(cls, book: BookInput) -> BookModel:
        print(f"\nBook inserted: {book.dict()}\n")
        book_model = BookModel(**book.dict())
        db.session.add(book_model)
        await db.session.flush()
        return book_model
