from fastapi import Request
from fastapi.responses import JSONResponse

from .exception import BaseHTTPException


def base_http_exception_handler(_: Request, exception: BaseHTTPException):
    response = {"detail": exception.detail}
    return JSONResponse(response, status_code=exception.status_code)
