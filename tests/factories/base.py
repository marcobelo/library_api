from abc import abstractmethod
from dataclasses import dataclass
from typing import Dict, List, Optional, Union

from faker import Faker

from src.schema.base import ORMBaseModel
from tests.config import create_mixer


@dataclass
class BaseFakeResult:
    data: Dict
    model: Optional[ORMBaseModel]
    expected: Dict


class BaseFakeFactory:
    fk = Faker()
    mx = create_mixer()
    input_data: Union[List[Dict], int] = None
    save: bool = None
    fake_result = None

    def create_items(self):
        if isinstance(self.input_data, int):
            return [self.create_item() for _ in range(self.input_data)]
        else:
            return [self.create_item(item) for item in self.input_data]

    def create_item(self, data: Dict = None):
        item_data = self.create_data(data)
        item_model = None
        if self.save:
            item_model = self.create_model(item_data)
        item_expected = self.create_expected(item_data, item_model)
        return self.fake_result(data=item_data, model=item_model, expected=item_expected)

    def create_data(self, data: Dict) -> Dict:
        if data is None:
            data = {}
        return self.randomize(data)

    @abstractmethod
    def randomize(self, data):
        pass

    @abstractmethod
    def create_model(self, data):
        pass

    @staticmethod
    @abstractmethod
    def create_expected(data, model):
        pass
