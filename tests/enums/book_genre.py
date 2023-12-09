from .domain_base import Domain, DomainBaseEnum


class BookGenreEnum(DomainBaseEnum):
    FICTION = Domain(
        id=1,
        code="FICTION",
        title="Fiction",
        seq=1,
    )
    SCIENCE_FICTION = Domain(
        id=2,
        code="SCIENCE_FICTION",
        title="Science Fiction",
        seq=2,
    )
    HISTORICAL_FICTION = Domain(
        id=3,
        code="HISTORICAL_FICTION",
        title="Historical Fiction",
        seq=3,
    )
    ROMANCE = Domain(
        id=4,
        code="ROMANCE",
        title="Romance",
        seq=4,
    )
    FANTASY = Domain(
        id=5,
        code="FANTASY",
        title="Fantasy",
        seq=5,
    )
