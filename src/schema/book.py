import uuid
from datetime import datetime

from pydantic import BaseModel
from sqlalchemy import Boolean, Column, DateTime, ForeignKey, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from src.config.database import Base

from .custom_fields import ISBN
from .domain import DomainModel, DomainOutput


class BookModel(Base):
    __tablename__ = "book"

    guid = Column(UUID(as_uuid=True), primary_key=True, nullable=False, default=uuid.uuid4)
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
        schema_extra = {
            "example": {
                "title": "The book",
                "author": "Marco Belo",
                "isbn": "978-3-16-148410-0",
                "id_genre": 4,
            }
        }


class BookOutput(BaseModel):
    guid: uuid.UUID
    title: str
    author: str
    isbn: ISBN
    genre: DomainOutput

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "guid": "5adf2183-e6e2-4254-8593-1db885394c89",
                "title": "The book",
                "author": "Marco Belo",
                "isbn": "978-3-16-148410-0",
            }
        }
