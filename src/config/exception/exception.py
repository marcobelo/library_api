from fastapi import HTTPException, status


class BaseHTTPException(HTTPException):
    def __init__(
        self, status_code: int = status.HTTP_500_INTERNAL_SERVER_ERROR, detail: str = "Internal Server Error"
    ) -> None:
        self.status_code = status_code
        self.detail = detail


class NotFoundException(BaseHTTPException):
    def __init__(self, detail: str = "Not Found"):
        super().__init__(status_code=status.HTTP_404_NOT_FOUND, detail=detail)
