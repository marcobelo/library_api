from fastapi import Request


async def async_sessionmaker(request: Request):
    return request.scope.get("async_sessionmaker")
