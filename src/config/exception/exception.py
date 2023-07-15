from fastapi import HTTPException, status


class BaseHTTPException(HTTPException):
    def __init__(
        self,
        status_code: int = status.HTTP_500_INTERNAL_SERVER_ERROR,
        detail: str = "Internal Server Error",
        log: str = "",
        log_level: str = "info",
    ) -> None:
        self.status_code = status_code
        self.detail = detail
        self.log = log
        self.log_level = log_level


class NotFoundException(BaseHTTPException):
    def __init__(self, detail: str = "Not Found", log: str = ""):
        super().__init__(status_code=status.HTTP_404_NOT_FOUND, detail=detail, log=log)


class MissingEnvironmentException(Exception):
    """This error is only raised when starting the system, it's not a http exception"""

    pass
