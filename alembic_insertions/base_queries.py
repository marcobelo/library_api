from abc import abstractmethod
from typing import Dict, List, Union

from sqlalchemy import text
from sqlalchemy.engine import CursorResult
from sqlalchemy.orm import Session

from alembic import op


class BaseQueries:
    def __init__(self, __op: op) -> None:
        self.__make_session(__op)

    def __make_session(self, __op: op) -> None:
        bind = __op.get_bind()
        self.__session = Session(bind=bind)

    def commit(self) -> None:
        self.__session.commit()

    def flush(self) -> None:
        self.__session.flush()

    def execute(self, query: text, values: Union[Dict, List[Dict]]) -> CursorResult:
        result = self.__session.execute(query, values)
        self.flush()
        return result

    @abstractmethod
    def upgrade(self) -> None:
        pass

    @abstractmethod
    def downgrade(self) -> None:
        pass

    @staticmethod
    @abstractmethod
    def get_table_values() -> Dict:
        pass

    def insert_into(self, table: str, items: List[Dict]) -> None:
        item = items[0]
        fields = ",".join(item.keys())
        values = ",".join([":" + f for f in item.keys()])
        query = text(f"INSERT INTO {table} ({fields}) VALUES ({values})")
        self.execute(query, items)

    def remove_from(self, table: str, items: List[Dict]) -> None:
        for item in items:
            for k, v in item.items():
                if isinstance(v, str):
                    item[k] = f"'{v}'"
            where = " AND ".join([f"{k}={v}" for k, v in item.items()])
            query = text(f"DELETE FROM {table} WHERE {where}")
            self.execute(query, item)
