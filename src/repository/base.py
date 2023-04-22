from src.config.database import db


class BaseRepository:
    def __init__(self, database):
        self.session = database.session
        # TODO: move database operations here
