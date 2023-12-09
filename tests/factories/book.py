from copy import deepcopy
from dataclasses import dataclass
from random import choice
from typing import Dict, List, Optional, Union

from src.schema import BookModel
from tests.enums import BookGenreEnum
from tests.factories.base import BaseFakeFactory, BaseFakeResult


@dataclass
class BookFakeResult(BaseFakeResult):
    model: Optional[BookModel]


class BookFakeFactory(BaseFakeFactory):
    def __init__(self, books: Union[List[Dict], int], save: bool = True):
        self.input_data = books
        self.save = save
        self.fake_result = BookFakeResult

    def new(self) -> List[BookFakeResult]:
        return self.create_items()

    def randomize(self, data: Dict) -> Dict:
        result = {
            "title": data.get("title", self.fk.sentence()),
            "isbn": data.get("isbn", self.fk.isbn13(separator="-")),
            "id_genre": data.get("id_genre", choice(list(BookGenreEnum)).id),
        }
        if data.get("guid"):
            result["guid"] = data["guid"]
        return result

    def create_model(self, data: Dict) -> BookModel:
        return self.mx.blend(BookModel, **data)

    @staticmethod
    def create_expected(data: Dict, model: BookModel) -> Dict:
        expected = deepcopy(data)
        del expected["id_genre"]
        expected["genre"] = BookGenreEnum.get_enum_by_id(data["id_genre"]).dict
        if model:
            expected["id"] = model.id
            expected["guid"] = str(model.guid)
        return expected
