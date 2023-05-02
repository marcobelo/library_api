from .exception import BaseHTTPException, MissingEnvironmentException, MissingSessionException, NotFoundException
from .handler import base_http_exception_handler

EXCEPTIONS_AND_HANDLERS = [
    (BaseHTTPException, base_http_exception_handler),
    (NotFoundException, base_http_exception_handler),
]
