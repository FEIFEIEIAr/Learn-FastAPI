import os.path
from pydantic import BaseSettings
from typing import List


class Config(BaseSettings):
    # 调试模式
    APP_DEBUG: bool = True
    # 项目信息
    VERSION: str = "0.0.1"
    PROJECT_NAME: str = "Learning FastAPI"
    DESCRIPTION: str = 'Things to learn about FastAPI'
    # 静态资源目录
    STATIC_DIR: str = os.path.join(os.getcwd(), "static")
    # 跨域请求
    CORS_ORIGINS: List[str] = ['*']
    CORS_ALLOW_CREDENTIALS: bool = True
    CORS_ALLOW_METHODS: List[str] = ['*']
    CORS_ALLOW_HEADERS: List[str] = ['*']


settings = Config()
