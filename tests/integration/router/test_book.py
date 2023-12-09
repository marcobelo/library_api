import math
from uuid import uuid4

from fastapi import status
from hamcrest import assert_that, has_entries

from src.schema import BookModel
from tests.factories import BookFakeFactory


class TestBookController:
    def test_get_list_should_return_list_of_all_books_not_deleted_with_pagination(self, api_client):
        page, page_size, num_items = 2, 2, 11
        pages = math.ceil(num_items / page)
        books = BookFakeFactory(num_items).new()

        response = api_client.get("/books", params={"page": page, "size": page_size})

        response_json = response.json()
        items = response_json.pop("items")
        assert response.status_code == status.HTTP_200_OK
        assert_that(response_json, has_entries({"total": num_items, "page": page, "size": page_size, "pages": pages}))
        assert_that(items[0], has_entries({**books[8].expected}))
        assert_that(items[1], has_entries({**books[7].expected}))

    def test_post_should_create_new_book_register(self, api_client):
        book = BookFakeFactory(1, False).new()[0]

        response = api_client.post("/books", json=book.data)

        assert response.status_code == status.HTTP_201_CREATED
        assert_that(response.json(), has_entries(book.expected))

    def test_delete_should_mark_a_book_as_deleted(self, api_client, db_session):
        book = BookFakeFactory(1).new()[0]

        response = api_client.delete(f"/books/{book.model.guid}")

        deleted_book = db_session.query(BookModel).filter(BookModel.guid == book.model.guid).first()
        assert response.status_code == status.HTTP_204_NO_CONTENT
        assert deleted_book.deleted

    def test_delete_should_return_not_found_if_guid_dont_exist(self, api_client):
        book_guid = str(uuid4())

        response = api_client.delete(f"/books/{book_guid}")

        assert response.status_code == status.HTTP_404_NOT_FOUND
        assert response.json() == {"detail": "Not Found"}
