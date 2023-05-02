from pydantic import ValidationError
from pytest import raises

from src.schema import BookInput, BookOutput


class TestBookSchemas:
    def test_validate_input_required_fields(self, unpack_validation_error):
        with raises(ValidationError) as exc:
            BookInput()
        result = unpack_validation_error(exc)
        expected = [
            {"loc": ["title"], "msg": "field required", "type": "value_error.missing"},
            {"loc": ["author"], "msg": "field required", "type": "value_error.missing"},
            {"loc": ["isbn"], "msg": "field required", "type": "value_error.missing"},
            {"loc": ["id_genre"], "msg": "field required", "type": "value_error.missing"},
        ]
        assert result == expected

    def test_validate_output_required_fields(self, unpack_validation_error):
        with raises(ValidationError) as exc:
            BookOutput()
        result = unpack_validation_error(exc)
        expected = [
            {"loc": ["guid"], "msg": "field required", "type": "value_error.missing"},
            {"loc": ["title"], "msg": "field required", "type": "value_error.missing"},
            {"loc": ["author"], "msg": "field required", "type": "value_error.missing"},
            {"loc": ["isbn"], "msg": "field required", "type": "value_error.missing"},
            {"loc": ["genre"], "msg": "field required", "type": "value_error.missing"},
        ]
        assert result == expected
