from src.schema import BookInput, BookOutput


class BookController:
    @classmethod
    async def add_book(cls, book: BookInput) -> BookOutput:
        print(f"\nBook inserted: {book.dict()}\n")
        return BookOutput(**book.dict())
