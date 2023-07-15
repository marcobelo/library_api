from copy import deepcopy
from dataclasses import dataclass
from random import choice
from typing import Dict, List, Optional, Union

from src.schema import BookModel
from tests.enums import BookGenreEnum
from tests.factories.base import BaseFakeFactory


@dataclass
class BookFakeResult:
    data: Dict
    model: Optional[BookModel]
    expected: Dict


class BookFakeFactory(BaseFakeFactory):
    @classmethod
    def new(cls, books: Union[List[Dict], int], save: bool = True) -> List[BookFakeResult]:
        created_books = []
        if isinstance(books, int):
            for _ in range(books):
                created_books.append(cls.__new_item(save))
        else:
            for book in books:
                created_books.append(cls.__new_item(save, book))
        return created_books

    @classmethod
    def __new_item(cls, save: bool, data: Dict = None) -> BookFakeResult:
        book_data = cls.__create_data(data)
        book_model = None
        if save:
            book_model = cls.__create_model(book_data)
        book_expected = cls.__create_expected(book_data, book_model)
        return BookFakeResult(data=book_data, model=book_model, expected=book_expected)

    @classmethod
    def __create_data(cls, data: Dict) -> Dict:
        if data is None:
            data = {}
        return cls.__randomize(data)

    @classmethod
    def __create_model(cls, book_data: Dict) -> BookModel:
        return cls.mx.blend(BookModel, **book_data)

    @staticmethod
    def __create_expected(book_data: Dict, book_model: BookModel) -> Dict:
        expected = deepcopy(book_data)
        del expected["id_genre"]
        expected["genre"] = BookGenreEnum.get_enum_by_id(book_data["id_genre"]).dict
        if book_model:
            expected["id"] = book_model.id
            expected["guid"] = str(book_model.guid)
        return expected

    @classmethod
    def __randomize(cls, data: Dict) -> Dict:
        result = {
            "title": data.get("title", cls.fk.sentence()),
            "author": data.get("author", cls.fk.name()),
            "isbn": data.get("isbn", cls.fk.isbn13(separator="-")),
            "id_genre": data.get("id_genre", choice(list(BookGenreEnum)).id),
        }
        if data.get("guid"):
            result["guid"] = data["guid"]
        return result
