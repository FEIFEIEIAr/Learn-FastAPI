from fastapi import APIRouter

from app.api.Login import login, index
from app.api.test_redis import test_my_redis, test_my_redis_depends

ApiRouter = APIRouter(prefix="/v1", tags=["api路由"])


@ApiRouter.get('/input')
async def home(num: int):
    return {"num": num, "data": [{"num": num, "data": []}, {"num": num, "data": []}]}


ApiRouter.get("/index", tags=["api路由"], summary="注册接口")(index)

ApiRouter.post("/login", tags=["api路由"], summary="登陆接口")(login)

# FastAPI中两种Redis的使用方式
ApiRouter.get("/test/my/redis", tags=["api路由"], summary="fastapi的state方式")(test_my_redis)
ApiRouter.get("/test/my/redis/depends", tags=["api路由"], summary="依赖注入方式")(test_my_redis_depends)