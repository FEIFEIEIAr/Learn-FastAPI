import os
from fastapi import FastAPI, HTTPException
from fastapi.exceptions import RequestValidationError
from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware.sessions import SessionMiddleware
from config import settings
from fastapi.staticfiles import StaticFiles
from app.api.Base import router
from app.core.Events import startup, stopping
from app.core.Exception import http_error_handler, http422_error_handler, unicorn_exception_handler, UnicornException
from app.core.Middleware import Middleware

application = FastAPI(
    debug=settings.APP_DEBUG,
    description=settings.DESCRIPTION,
    version=settings.VERSION,
    title=settings.PROJECT_NAME
    )

# 事件监听
# 当application启动时，执行startup函数
application.add_event_handler("startup", startup(application))
# 当application关闭时，执行stopping函数
application.add_event_handler("shutdown", stopping(application))

# 异常错误处理
# 重写异常处理函数。前面的是参数，后面的是函数
application.add_exception_handler(HTTPException, http_error_handler)
application.add_exception_handler(RequestValidationError, http422_error_handler)
application.add_exception_handler(UnicornException, unicorn_exception_handler)

# 路由
application.include_router(router)

# 中间件
application.add_middleware(Middleware)
application.add_middleware(
    SessionMiddleware,
    secret_key="session",
    session_cookie="f_id",
    # max_age=4
)
application.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=settings.CORS_ALLOW_CREDENTIALS,
    allow_methods=settings.CORS_ALLOW_METHODS,
    allow_headers=settings.CORS_ALLOW_HEADERS,
)

# 静态资源目录
application.mount('/static', StaticFiles(directory=os.path.join(os.getcwd(), "static")))

app = application


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", reload=True)