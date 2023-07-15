from dataclasses import asdict
from enum import Enum


class BaseEnum(Enum):
    @property
    def id(self):
        return self.value.id

    @property
    def dict(self):
        return asdict(self.value)
