from sqlalchemy.orm import Session

from alembic_insertions.domain import DomainV0

from .base_inserter import BaseInserter


class InserterV0(BaseInserter):
    @staticmethod
    def insertions(session: Session):
        DomainV0(session)
