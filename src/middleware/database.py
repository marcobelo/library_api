from starlette.types import ASGIApp, Receive, Scope, Send

from src.config.database import db, make_async_session


class DatabaseMiddleware:
    def __init__(self, app: ASGIApp) -> None:
        self.app = app

    async def __call__(self, scope: Scope, receive: Receive, send: Send) -> None:
        try:
            async_session = await make_async_session()
            async with async_session() as session:
                db.set_session(session)
                async with session.begin():
                    await self.app(scope, receive, send)
                db.set_session(None)
            async_session.close_all()
        except Exception as ex:
            print(ex)


config = {}
DATABASE_MIDDLEWARE = (DatabaseMiddleware, config)
