from pydantic import BaseModel

from .custom_fields import ISBN


class BookInput(BaseModel):
    title: str
    author: str
    isbn: ISBN

    class Config:
        schema_extra = {
            "example": {
                "title": "O livro",
                "author": "Marco Belo",
                "isbn": "978-3-16-148410-0",
            }
        }


class BookOutput(BaseModel):
    title: str
    author: str
    isbn: ISBN

    class Config:
        schema_extra = {
            "example": {
                "title": "O livro",
                "author": "Marco Belo",
                "isbn": "978-3-16-148410-0",
            }
        }
