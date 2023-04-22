from fastapi import Depends, status
from fastapi_utils.cbv import cbv
from fastapi_utils.inferring_router import InferringRouter
from sqlalchemy.orm import Session

from src.config.database import db
from src.controller import BookController
from src.schema import BookInput, BookOutput

router = InferringRouter(tags=["Book"])


@cbv(router)
class BookRouter:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.controller = BookController

    @router.post("/books", response_model=BookOutput, status_code=status.HTTP_201_CREATED)
    async def post_book(self, book: BookInput):
        return await self.controller.add_book(book)
