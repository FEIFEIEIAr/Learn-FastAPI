"""
test redis
"""

from app.core.Response import success
from fastapi import Depends, Request
from app.database.Redis import sys_cache
from aioredis import Redis


async def test_my_redis(request: Request):
    # 连接池放在request
    value = await request.app.state.cache.get("today")

    return success(msg="test_my_redis", data=[value])


async def test_my_redis_depends(today: int, cache: Redis = Depends(sys_cache)):
    # 连接池放在依赖注入
    # await cache.set(name="today", value=today)
    # # await cache.set(name="ex_today", value=today, ex=60)  # 过期的key
    # return success(msg="今天是{}号".format(today), data=[])
    
    
    value = await cache.get("today")
    return success(msg="今天是{}号".format(today), data=[value])