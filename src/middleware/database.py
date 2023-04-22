from starlette.types import ASGIApp, Receive, Scope, Send

from src.config.database import make_async_session, session_holder


class DatabaseMiddleware:
    def __init__(self, app: ASGIApp) -> None:
        self.app = app

    async def __call__(self, scope: Scope, receive: Receive, send: Send) -> None:
        try:
            async_session = await make_async_session()
            async with async_session() as session:
                session_token = session_holder.set(session)
                async with session.begin():
                    await self.app(scope, receive, send)
                session_holder.reset(session_token)
        except Exception as ex:
            print(ex)


config = {}
DATABASE_MIDDLEWARE = (DatabaseMiddleware, config)
