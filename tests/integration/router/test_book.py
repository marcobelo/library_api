from uuid import uuid4

from fastapi import status
from hamcrest import assert_that, has_entries

from src.schema import BookModel
from tests.enums import BookGenreEnum
from tests.factories import BookFakerFactory


class TestBookController:
    def test_post_should_create_new_book_register(self, api_client):
        payload = BookFakerFactory.new(id_genre=BookGenreEnum.FICTION.id)

        response = api_client.post("/books", json=payload)
        expected = {**payload, "genre": BookGenreEnum.FICTION.dict}
        del expected["id_genre"]

        assert response.status_code == status.HTTP_201_CREATED
        assert_that(response.json(), has_entries(expected))

    def test_delete_should_mark_a_book_as_deleted(self, api_client, mixer, db_session):
        guid_book = str(uuid4())
        mixer.blend(BookModel, **BookFakerFactory.new(id_genre=BookGenreEnum.FICTION.id, guid=guid_book))

        response = api_client.delete(f"/books/{guid_book}")
        assert response.status_code == status.HTTP_204_NO_CONTENT

        deleted_book = db_session.query(BookModel).first()
        assert deleted_book.deleted
