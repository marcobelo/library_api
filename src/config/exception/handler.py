from fastapi import Request
from fastapi.responses import JSONResponse

from src.config.logger import logger

from .exception import BaseHTTPException


def base_http_exception_handler(_: Request, exception: BaseHTTPException):
    response = {"detail": exception.detail}
    if exception.log:
        getattr(logger, exception.log_level)(exception.log)
    return JSONResponse(response, status_code=exception.status_code)
