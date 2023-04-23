from typing import Callable, List, Tuple, Type

from fastapi import FastAPI
from fastapi_utils.inferring_router import InferringRouter

from src.config.exception import EXCEPTIONS_AND_HANDLERS
from src.middleware import MIDDLEWARES
from src.router import ROUTERS


class CreateApp:
    def __init__(
        self,
        routers: List[InferringRouter] = ROUTERS,
        exceptions_and_handlers: List[Tuple[Type[Exception], Callable]] = EXCEPTIONS_AND_HANDLERS,
    ) -> None:
        self.__app = FastAPI()
        self.__routers = routers
        self.__exceptions_and_handlers = exceptions_and_handlers

    def execute(self) -> FastAPI:
        self.__add_routers()
        self.__add_exception_handlers()
        self.__add_middlewares()
        return self.__app

    def __add_routers(self) -> None:
        for router in self.__routers:
            self.__app.include_router(router)

    def __add_exception_handlers(self) -> None:
        for exception, handler in self.__exceptions_and_handlers:
            self.__app.add_exception_handler(exception, handler)

    def __add_middlewares(self) -> None:
        for middleware, config in MIDDLEWARES:
            self.__app.add_middleware(middleware, **config)


create_app = CreateApp()
app = create_app.execute()

# TODO: Add logging and change prints for logs
