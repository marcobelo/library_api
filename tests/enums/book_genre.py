from .domain_base import Domain, DomainBaseEnum


class BookGenreEnum(DomainBaseEnum):
    FICTION = Domain(id=1, code="FICTION", title="Fiction")
    SCIENCE_FICTION = Domain(id=2, code="SCIENCE_FICTION", title="Science Fiction")
    HISTORICAL_FICTION = Domain(id=3, code="HISTORICAL_FICTION", title="Historical Fiction")
    ROMANCE = Domain(id=4, code="ROMANCE", title="Romance")
    FANTASY = Domain(id=5, code="FANTASY", title="Fantasy")
