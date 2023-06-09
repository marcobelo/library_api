from faker import Faker

from tests.enums import BookGenreEnum


class BookFakerFactory:
    @classmethod
    def new(
        cls,
        title: str = None,
        author: str = None,
        isbn: str = None,
        id_genre: int = BookGenreEnum.FICTION.id,
        guid: str = None,
    ) -> dict:
        fake = Faker()
        data = {
            "title": title or fake.sentence(),
            "author": author or fake.name(),
            "isbn": isbn or fake.isbn13(separator="-"),
            "id_genre": id_genre or 1,
        }
        if guid:
            data["guid"] = guid
        return data
