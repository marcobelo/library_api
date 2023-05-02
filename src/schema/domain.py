from typing import Optional

from pydantic import BaseModel
from sqlalchemy import Column, Integer, String

from src.config.database import Base


class DomainModel(Base):
    __tablename__ = "domain"

    id = Column(Integer, primary_key=True, nullable=False)
    table = Column(String)
    field = Column(String)
    code = Column(String)
    title = Column(String)
    order = Column(Integer)


class DomainInput(BaseModel):
    table: str
    field: str
    code: str
    title: str
    order: Optional[int]

    class Config:
        schema_extra = {
            "example": {
                "table": "book",
                "field": "id_genre",
                "code": "HORROR",
                "title": "Horror",
                "order": 6,
            }
        }


class DomainOutput(BaseModel):
    id: int
    table: str
    field: str
    code: str
    title: str
    order: Optional[int]

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "id": 3,
                "table": "book",
                "field": "id_genre",
                "code": "HORROR",
                "title": "Horror",
                "order": 6,
            }
        }
