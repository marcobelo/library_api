from alembic_insertions.base_queries import BaseQueries


class V1Queries(BaseQueries):
    def upgrade(self):
        for table, values in self.get_table_values().items():
            self.insert_into(table, values)

    def downgrade(self):
        for table, values in self.get_table_values().items():
            self.remove_from(table, values)

    @staticmethod
    def get_table_values():
        book_id_genre = {"source": "book", "field": "id_genre"}
        return {
            "domain": [
                {**book_id_genre, "code": "FICTION", "title": "Fiction"},
                {**book_id_genre, "code": "SCIENCE_FICTION", "title": "Science Fiction"},
                {**book_id_genre, "code": "HISTORICAL_FICTION", "title": "Historical Fiction"},
                {**book_id_genre, "code": "ROMANCE", "title": "Romance"},
                {**book_id_genre, "code": "FANTASY", "title": "Fantasy"},
                {**book_id_genre, "code": "MYSTERY", "title": "Mystery"},
                {**book_id_genre, "code": "HORROR", "title": "Horror"},
                {**book_id_genre, "code": "THRILLER", "title": "Thriller"},
                {**book_id_genre, "code": "BIOGRAPHY", "title": "Biography"},
                {**book_id_genre, "code": "POETRY", "title": "Poetry"},
            ]
        }
