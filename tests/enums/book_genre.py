from .domain_base import Domain, DomainBaseEnum


class BookGenreEnum(DomainBaseEnum):
    FICTION = Domain(
        id=1,
        code="FICTION",
        title="Fiction",
        order=None,
    )
    SCIENCE_FICTION = Domain(
        id=2,
        code="SCIENCE_FICTION",
        title="Science Fiction",
        order=None,
    )
    HISTORICAL_FICTION = Domain(
        id=3,
        code="HISTORICAL_FICTION",
        title="Historical Fiction",
        order=None,
    )
    ROMANCE = Domain(
        id=4,
        code="ROMANCE",
        title="Romance",
        order=None,
    )
    FANTASY = Domain(
        id=5,
        code="FANTASY",
        title="Fantasy",
        order=None,
    )
