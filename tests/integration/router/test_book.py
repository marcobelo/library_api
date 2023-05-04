from uuid import uuid4

from fastapi import status
from hamcrest import assert_that, has_entries

from src.schema import BookModel
from tests.enums import BookGenreEnum
from tests.factories import BookFakerFactory


class TestBookController:
    def test_get_list_should_return_list_of_all_books_not_deleted_with_pagination(self, api_client, mixer):
        fiction_book = BookFakerFactory.new(id_genre=BookGenreEnum.FICTION.id)
        historical_book = BookFakerFactory.new(id_genre=BookGenreEnum.HISTORICAL_FICTION.id)
        mixer.blend(BookModel, **BookFakerFactory.new(id_genre=BookGenreEnum.SCIENCE_FICTION.id))
        mixer.blend(BookModel, **fiction_book)
        mixer.blend(BookModel, **historical_book)
        mixer.blend(BookModel, **BookFakerFactory.new(id_genre=BookGenreEnum.ROMANCE.id))
        mixer.blend(BookModel, **BookFakerFactory.new(id_genre=BookGenreEnum.FANTASY.id))
        params = {"page": 2, "size": 2}

        response = api_client.get("/books", params=params)
        response_json = response.json()
        items = response_json.pop("items")
        del historical_book["id_genre"]
        del fiction_book["id_genre"]

        assert_that(items[0], has_entries({**historical_book, "id": 3, "genre": BookGenreEnum.HISTORICAL_FICTION.dict}))
        assert_that(items[1], has_entries({**fiction_book, "id": 2, "genre": BookGenreEnum.FICTION.dict}))
        assert_that(response_json, has_entries({"total": 5, "page": 2, "size": 2, "pages": 3}))

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
        deleted_book = db_session.query(BookModel).first()

        assert response.status_code == status.HTTP_204_NO_CONTENT
        assert deleted_book.deleted

    def test_delete_should_return_not_found_if_guid_dont_exist(self, api_client, mixer, db_session):
        guid_book = str(uuid4())

        response = api_client.delete(f"/books/{guid_book}")

        assert response.status_code == status.HTTP_404_NOT_FOUND
        assert response.json() == {"detail": "Not Found"}
