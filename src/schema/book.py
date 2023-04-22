from uuid import UUID, uuid4

from pydantic import BaseModel
from sqlalchemy import Column, String
from sqlalchemy.dialects.postgresql import UUID as pg_UUID

from src.config.database import Base

from .custom_fields import ISBN


class BookModel(Base):
    __tablename__ = "book"

    guid = Column(pg_UUID(as_uuid=True), primary_key=True, nullable=False, default=uuid4)
    title = Column(String)
    author = Column(String)
    isbn = Column(String)


class BookInput(BaseModel):
    title: str
    author: str
    isbn: ISBN

    class Config:
        schema_extra = {
            "example": {
                "title": "O livro",
                "author": "Marco Belo",
                "isbn": "978-3-16-148410-0",
            }
        }


class BookOutput(BaseModel):
    guid: UUID
    title: str
    author: str
    isbn: ISBN

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "guid": "5adf2183-e6e2-4254-8593-1db885394c89",
                "title": "O livro",
                "author": "Marco Belo",
                "isbn": "978-3-16-148410-0",
            }
        }
