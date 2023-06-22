import uuid
from datetime import datetime

from pydantic import BaseModel, Extra
from sqlalchemy import Boolean, Column, DateTime, Integer
from sqlalchemy.dialects.postgresql import UUID

from src.config.database import Base


class ORMBaseModel(Base):
    __abstract__ = True

    id = Column(Integer, primary_key=True, nullable=False)
    guid = Column(UUID(as_uuid=True), nullable=False, default=uuid.uuid4, unique=True)
    deleted = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)


class BaseInput(BaseModel):
    class Config:
        extra = Extra.forbid


class BaseOutput(BaseModel):
    class Config:
        orm_mode = True
