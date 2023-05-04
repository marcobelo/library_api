import uuid
from datetime import datetime

from pydantic import BaseModel, Extra
from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from src.config.database import Base

from .custom_fields import ISBN
from .domain import DomainModel, DomainOutput


class BookModel(Base):
    __tablename__ = "book"

    id = Column(Integer, primary_key=True, nullable=False)
    guid = Column(UUID(as_uuid=True), nullable=False, default=uuid.uuid4, unique=True)
    title = Column(String)
    author = Column(String)
    isbn = Column(String)
    id_genre = Column(ForeignKey(DomainModel.id))
    genre = relationship(DomainModel, foreign_keys=[id_genre], lazy="joined")

    deleted = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)


class BookInput(BaseModel):
    title: str
    author: str
    isbn: ISBN
    id_genre: int

    class Config:
        extra = Extra.forbid
        schema_extra = {
            "example": {
                "title": "The book",
                "author": "Marco Belo",
                "isbn": "978-3-16-148410-0",
                "id_genre": 4,
            }
        }


class BookOutput(BaseModel):
    id: int
    guid: uuid.UUID
    title: str
    author: str
    isbn: ISBN
    genre: DomainOutput

    class Config:
        orm_mode = True
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
                    "order": None,
                },
            }
        }
