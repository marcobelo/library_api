from hamcrest import assert_that, has_entries

from src.schema import BookInput


class TestBookController:
    def test_post_should_create_new_book_register(self, api_client):
        payload = {"title": "Book 1", "author": "Tester", "isbn": "978-3-16-148410-0"}
        response = api_client.post("/books", json=payload)
        response_json = response.json()

        assert response.status_code == 201
        assert_that(response_json, has_entries(payload))
