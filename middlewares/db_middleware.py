from typing import Callable, Dict, Any, Awaitable
from aiogram import BaseMiddleware
from database.db import async_session


class DbSessionMiddleware(BaseMiddleware):
    async def __call__(
        self,
        handler: Callable,
        event: Any,
        data: Dict[str, Any],
    ) -> Awaitable[Any]:
        async with async_session() as session:
            data["session"] = session
            return await handler(event, data)
