from uuid import UUID

from fastapi import Depends, status
from fastapi_pagination import Params as PaginationParams
from fastapi_utils.cbv import cbv
from fastapi_utils.inferring_router import InferringRouter
from sqlalchemy.ext.asyncio import AsyncSession

from src.controller import BookController
from src.repository import BookRepository
from src.schema import BookInput, BookOutput, PaginateOutput

from .dependencies import async_session

router = InferringRouter(tags=["Book"])


@cbv(router)
class BookRouter:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.book_repository = BookRepository()
        self.book_controller = BookController(self.book_repository)

    @router.get("/books", response_model=PaginateOutput[BookOutput], status_code=status.HTTP_200_OK)
    async def list_books(self, params: PaginationParams = Depends(), session: AsyncSession = Depends(async_session)):
        self.book_repository.set_session(session)
        return await self.book_controller.get_books(params)

    @router.post("/books", response_model=BookOutput, status_code=status.HTTP_201_CREATED)
    async def create_book(self, book_input: BookInput, session: AsyncSession = Depends(async_session)):
        self.book_repository.set_session(session)
        return await self.book_controller.add_book(book_input)

    @router.delete("/books/{book_guid}", status_code=status.HTTP_204_NO_CONTENT)
    async def delete_book(self, book_guid: UUID, session: AsyncSession = Depends(async_session)):
        self.book_repository.set_session(session)
        await self.book_controller.delete_book(book_guid)
