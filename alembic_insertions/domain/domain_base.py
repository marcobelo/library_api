from abc import abstractmethod
from typing import List

from sqlalchemy.orm import Session

from src.schema.domain import DomainInput, DomainModel


class DomainBase:
    def __init__(self, session: Session) -> None:
        self.session = session
        domains = self.create_input_schemas()
        for domain in domains:
            new_domain = DomainModel(**domain.dict())
            self.session.add(new_domain)

    @abstractmethod
    def create_input_schemas(self) -> List[DomainInput]:
        pass

    @staticmethod
    def new(table: str, field: str, code: str, title: str, order: int = None) -> DomainInput:
        domain_data = {
            "table": table,
            "field": field,
            "code": code,
            "title": title,
            "order": order,
        }
        return DomainInput(**domain_data)
