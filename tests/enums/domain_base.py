from dataclasses import dataclass
from typing import Optional

from tests.enums.base import BaseEnum


@dataclass
class Domain:
    id: int
    code: str
    title: str
    seq: Optional[int]


class DomainBaseEnum(BaseEnum):
    @classmethod
    def get_enum_by_id(cls, id_enum: int) -> Optional[BaseEnum]:
        for member in cls:
            if member.value.id == id_enum:
                return member
