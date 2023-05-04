from typing import Any, Callable, List, Tuple, Type

from fastapi import FastAPI
from fastapi_pagination import add_pagination
from fastapi_utils.inferring_router import InferringRouter

from src.config.exception import EXCEPTIONS_AND_HANDLERS
from src.middleware import MIDDLEWARES
from src.router import ROUTERS


class CreateApp:
    def __init__(
        self,
        routers: List[InferringRouter] = ROUTERS,
        exceptions_and_handlers: List[Tuple[Type[Exception], Callable]] = EXCEPTIONS_AND_HANDLERS,
        middlewares: List[Tuple[Any, dict]] = MIDDLEWARES,
    ) -> None:
        self.__app = FastAPI(**self.__app_config())
        self.__routers = routers
        self.__exceptions_and_handlers = exceptions_and_handlers
        self.__middlewares = middlewares

    def execute(self) -> FastAPI:
        self.__add_routers()
        self.__add_exception_handlers()
        self.__add_middlewares()
        self.__add_extras()
        return self.__app

    @staticmethod
    def __app_config() -> dict:
        return {
            "title": "Library API",
            "description": "API to manage books, authors and library daily operations",
            "version": "0.0.1",
            "contact": {
                "name": "Marco Belo",
                "url": "https://github.com/marcobelo",
                "email": "marco.barone.belo@gmail.com",
            },
            # "terms_of_service": "http://example.com/terms/",
            # license_info = {
            #     "name": "Apache 2.0",
            #     "url": "https://www.apache.org/licenses/LICENSE-2.0.html",
            # },
        }

    def __add_routers(self) -> None:
        for router in self.__routers:
            self.__app.include_router(router)

    def __add_exception_handlers(self) -> None:
        for exception, handler in self.__exceptions_and_handlers:
            self.__app.add_exception_handler(exception, handler)

    def __add_middlewares(self) -> None:
        for middleware, config in self.__middlewares:
            self.__app.add_middleware(middleware, **config)

    def __add_extras(self):
        add_pagination(self.__app)


create_app = CreateApp()
app = create_app.execute()
