from uuid import UUID

from fastapi_pagination import Page
from fastapi_pagination import Params as PaginationParams
from sqlalchemy.ext.asyncio import AsyncSession

from src.repository.base import BaseRepository
from src.schema import BookInput, BookModel


class BookRepository(BaseRepository):
    def __init__(self, session: AsyncSession = None) -> None:
        super().__init__(session, BookModel)

    async def list_books(self, params: PaginationParams) -> Page[BookModel]:
        filters = [BookModel.deleted == False]
        return await self.get_all_paginate(params, filters)

    async def add_book(self, book_input: BookInput) -> BookModel:
        book_model = BookModel(**book_input.dict())
        await self.add_one(book_model)
        return book_model

    async def delete_book(self, book_guid: UUID) -> None:
        filters = [BookModel.guid == book_guid]
        await self.delete_one(filters)
