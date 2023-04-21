from pydantic import Field, ValidationError, validator


class ISBN(str):
    alias = "ISBN"

    @classmethod
    def validate(cls, value: str) -> str:
        # TODO: validate ISBN format with regex
        return value
