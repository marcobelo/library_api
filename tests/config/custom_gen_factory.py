from mixer import mix_types
from mixer.backend.sqlalchemy import GenFactory
from sqlalchemy.dialects import postgresql


class CustomGenFactory(GenFactory):
    types = dict(GenFactory.types)
    types[postgresql.UUID] = mix_types.UUID
