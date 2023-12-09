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
                {**book_id_genre, "code": "FICTION", "title": "Fiction", "seq": 1},
                {**book_id_genre, "code": "SCIENCE_FICTION", "title": "Science Fiction", "seq": 2},
                {**book_id_genre, "code": "HISTORICAL_FICTION", "title": "Historical Fiction", "seq": 3},
                {**book_id_genre, "code": "ROMANCE", "title": "Romance", "seq": 4},
                {**book_id_genre, "code": "FANTASY", "title": "Fantasy", "seq": 5},
                {**book_id_genre, "code": "MYSTERY", "title": "Mystery", "seq": 6},
                {**book_id_genre, "code": "HORROR", "title": "Horror", "seq": 7},
                {**book_id_genre, "code": "THRILLER", "title": "Thriller", "seq": 8},
                {**book_id_genre, "code": "BIOGRAPHY", "title": "Biography", "seq": 9},
                {**book_id_genre, "code": "POETRY", "title": "Poetry", "seq": 10},
            ]
        }
