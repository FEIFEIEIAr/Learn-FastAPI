from typing import Callable
from fastapi import FastAPI

from app.database.Mysql import register_mysql
from app.database.Redis import sys_cache


def startup(app: FastAPI) -> Callable:
    """
    FastApi 启动完成事件
    :param app: FastAPI
    :return: start_app
    """
    async def app_start() -> None:
        # APP启动完成后触发
        print("网站启动")
        
        # 注册mysql数据库
        await register_mysql(app)
        
        # 注入缓存到app state
        app.state.cache = await sys_cache()
        
    return app_start


def stopping(app: FastAPI) -> Callable:
    """
    FastApi 停止事件
    :param app: FastAPI
    :return: stop_app
    """
    async def app_stop() -> None:
        # APP停止时触发
        print("网站关闭")
        
    return app_stop