import time
from starlette.datastructures import MutableHeaders
from starlette.types import ASGIApp, Receive, Scope, Send, Message
from fastapi import Request
from app.core.Utils import random_str


class Middleware:
    """
    Middleware
    """

    def __init__(
            self,
            app: ASGIApp,
    ) -> None:
        self.app = app

    async def __call__(self, scope: Scope, receive: Receive, send: Send) -> None:
        if scope["type"] != "http":  # pragma: no cover
            await self.app(scope, receive, send)
            return
        start_time = time.time()
        request = Request(scope, receive, send)  # 获取request
        if not request.session.get("session"):  # 如果session不存在则创建
            request.session.setdefault("session", random_str())  # 初始化session

        async def send_wrapper(message: Message) -> None:
            process_time = time.time() - start_time
            if message["type"] == "http.response.start":
                headers = MutableHeaders(scope=message)
                headers.append("X-Process-Time", str(process_time))
            await send(message)
        await self.app(scope, receive, send_wrapper)