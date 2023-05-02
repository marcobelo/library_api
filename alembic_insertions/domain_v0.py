from typing import List

from src.schema.domain import DomainInput

from .domain_base import DomainBase


class DomainV0(DomainBase):
    def create_input_schemas(self) -> List[DomainInput]:
        return [
            self.new("book", "id_genre", "FICTION", "Fiction"),
            self.new("book", "id_genre", "SCIENCE_FICTION", "Science Fiction"),
            self.new("book", "id_genre", "HISTORICAL_FICTION", "Historical Fiction"),
            self.new("book", "id_genre", "ROMANCE", "Romance"),
            self.new("book", "id_genre", "FANTASY", "Fantasy"),
            self.new("book", "id_genre", "MYSTERY", "Mystery"),
            self.new("book", "id_genre", "HORROR", "Horror"),
            self.new("book", "id_genre", "THRILLER", "Thriller"),
            self.new("book", "id_genre", "BIOGRAPHY", "Biography"),
            self.new("book", "id_genre", "POETRY", "Poetry"),
        ]
