from fastapi import Depends, status
from fastapi_utils.cbv import cbv
from fastapi_utils.inferring_router import InferringRouter
from sqlalchemy.orm import sessionmaker

from src.controller import BookController
from src.repository import BookRepository
from src.schema import BookInput, BookOutput

from .dependencies import async_sessionmaker

router = InferringRouter(tags=["Book"])


@cbv(router)
class BookRouter:
    @router.post("/books", response_model=BookOutput, status_code=status.HTTP_201_CREATED)
    async def post_book(self, book_input: BookInput, session_maker: sessionmaker = Depends(async_sessionmaker)):
        book_repository = BookRepository(session_maker)
        book_controller = BookController(book_repository)
        return await book_controller.add_book(book_input)
