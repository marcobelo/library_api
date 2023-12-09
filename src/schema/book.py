import uuid

from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.orm import relationship

from .base import BaseInput, BaseOutput, ORMBaseModel
from .custom_fields import ISBN
from .domain import DomainModel, DomainOutput


class BookModel(ORMBaseModel):
    __tablename__ = "book"

    title = Column(String)
    author = Column(String)
    isbn = Column(String)
    id_genre = Column(ForeignKey(DomainModel.id))
    genre = relationship(DomainModel, foreign_keys=[id_genre], lazy="joined")


class BookInput(BaseInput):
    title: str
    author: str
    isbn: ISBN
    id_genre: int

    class Config:
        schema_extra = {
            "example": {
                "title": "The book",
                "author": "Marco Belo",
                "isbn": "978-3-16-148410-0",
                "id_genre": 4,
            }
        }


class BookOutput(BaseOutput):
    id: int
    guid: uuid.UUID
    title: str
    author: str
    isbn: ISBN
    genre: DomainOutput

    class Config:
        schema_extra = {
            "example": {
                "id": 1,
                "guid": "e1fb3e12-2e18-4565-8ab2-4bdbb87da4ec",
                "title": "The book",
                "author": "Marco Belo",
                "isbn": "978-3-16-148410-0",
                "genre": {
                    "id": 4,
                    "code": "ROMANCE",
                    "title": "Romance",
                    "seq": 4,
                },
            }
        }
