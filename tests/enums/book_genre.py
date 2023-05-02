from .domain_base import Domain, DomainBaseEnum


class BookGenreEnum(DomainBaseEnum):
    FICTION = Domain(
        id=1,
        table="book",
        field="id_genre",
        title="Fiction",
        code="FICTION",
        order=None,
    )
