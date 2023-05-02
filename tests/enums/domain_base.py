from enum import Enum
from typing import Optional

from pydantic import BaseModel


class Domain(BaseModel):
    id: int
    table: str
    field: str
    title: str
    code: str
    order: Optional[str]


class DomainBaseEnum(Enum):
    @property
    def id(self):
        return self.value.id

    @property
    def dict(self):
        return self.value.dict()
