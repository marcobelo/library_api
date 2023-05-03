from abc import abstractmethod

from sqlalchemy.orm import Session

from alembic import op


class BaseInserter:
    def __init__(self, __op: op) -> None:
        bind = __op.get_bind()
        session = Session(bind=bind)
        self.insertions(session)
        session.commit()

    @staticmethod
    @abstractmethod
    def insertions(session: Session) -> None:
        pass
