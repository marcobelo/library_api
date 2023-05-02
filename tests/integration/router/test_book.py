from hamcrest import assert_that, has_entries

from tests.enums import BookGenreEnum
from tests.factories import BookFakerFactory


class TestBookController:
    def test_post_should_create_new_book_register(self, api_client):
        payload = BookFakerFactory.new(id_genre=BookGenreEnum.FICTION.id)

        response = api_client.post("/books", json=payload)
        expected = {**payload, "genre": BookGenreEnum.FICTION.dict}
        del expected["id_genre"]

        assert response.status_code == 201
        assert_that(response.json(), has_entries(expected))
