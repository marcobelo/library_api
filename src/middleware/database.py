from starlette.types import ASGIApp, Receive, Scope, Send

from src.config.database import get_async_sessionmaker


class DatabaseMiddleware:
    def __init__(self, app: ASGIApp) -> None:
        self.app = app

    async def __call__(self, scope: Scope, receive: Receive, send: Send) -> None:
        async_sessionmaker = await get_async_sessionmaker()
        scope["async_sessionmaker"] = async_sessionmaker
        await self.app(scope, receive, send)
        async_sessionmaker.close_all()


config = {}
DATABASE_MIDDLEWARE = (DatabaseMiddleware, config)
