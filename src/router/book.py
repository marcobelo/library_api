from fastapi import Depends, status
from fastapi_utils.cbv import cbv
from fastapi_utils.inferring_router import InferringRouter
from sqlalchemy.ext.asyncio import AsyncSession

from src.controller import BookController
from src.repository import BookRepository
from src.schema import BookInput, BookOutput

from .dependencies import async_session

router = InferringRouter(tags=["Book"])


@cbv(router)
class BookRouter:
    @router.post("/books", response_model=BookOutput, status_code=status.HTTP_201_CREATED)
    async def post_book(self, book_input: BookInput, session: AsyncSession = Depends(async_session)):
        book_repository = BookRepository(session)
        book_controller = BookController(book_repository)
        return await book_controller.add_book(book_input)
