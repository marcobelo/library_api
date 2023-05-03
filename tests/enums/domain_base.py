from dataclasses import asdict, dataclass
from enum import Enum
from typing import Optional


@dataclass
class Domain:
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
        return asdict(self.value)
