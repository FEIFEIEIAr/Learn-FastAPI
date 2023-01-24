from fastapi import APIRouter

from app.api.Login import login, index


ApiRouter = APIRouter(prefix="/v1", tags=["api路由"])


@ApiRouter.get('/input')
async def home(num: int):
    return {"num": num, "data": [{"num": num, "data": []}, {"num": num, "data": []}]}


ApiRouter.get("/index", tags=["api路由"], summary="注册接口")(index)

ApiRouter.post("/login", tags=["api路由"], summary="登陆接口")(login)
