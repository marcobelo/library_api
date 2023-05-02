import json
from typing import Callable

from pydantic import ValidationError
from pytest import fixture


@fixture(scope="function", name="unpack_validation_error")
def __fixture_unpack_validation_error() -> Callable:
    def __unpack_validation_error(exc: ValidationError):
        return json.loads(exc.value.json())

    return __unpack_validation_error
