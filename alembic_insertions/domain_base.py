from abc import abstractmethod
from typing import List

from sqlalchemy.orm import Session

from src.schema.domain import DomainInput, DomainModel


class DomainBase:
    """
    To call a DomainBase from an alembic migration script follow this steps:

    bind = op.get_bind()  # from alembic import op
    session = Session(bind=bind)  # from sqlalchemy.orm import Session
    domain_v0 = DomainV0(session)  # DomainV0 is a DomainBase subclass
    domain_v0.execute()
    session.commit()
    """

    def __init__(self, session: Session) -> None:
        self.session = session

    def execute(self) -> None:
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
