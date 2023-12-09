from typing import Optional

from pydantic import BaseModel, Extra
from sqlalchemy import Column, Integer, String

from src.config.database import Base


class DomainModel(Base):
    __tablename__ = "domain"

    id = Column(Integer, primary_key=True, nullable=False)
    code = Column(String, nullable=False)
    title = Column(String, nullable=False)
    seq = Column(Integer)

    # internal
    source = Column(String, nullable=False)
    field = Column(String, nullable=False)


class DomainInput(BaseModel):
    code: str
    title: str
    seq: Optional[int]

    source: str
    field: str

    class Config:
        extra = Extra.forbid
        schema_extra = {
            "example": {
                "source": "book",
                "field": "id_genre",
                "code": "HORROR",
                "title": "Horror",
                "seq": 6,
            }
        }


class DomainOutput(BaseModel):
    id: int
    code: str
    title: str
    seq: Optional[int]

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "id": 6,
                "code": "HORROR",
                "title": "Horror",
                "seq": 6,
            }
        }
