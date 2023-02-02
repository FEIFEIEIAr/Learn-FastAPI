from fastapi import APIRouter, Security

from app.api.Login import login, index
from app.api.test_redis import test_my_redis, test_my_redis_depends
from app.core.Auth import check_permissions
from app.api.User import user_info, user_add, user_del, get_user_rules


ApiRouter = APIRouter(prefix="/v1", tags=["api路由"])


ApiRouter.get("/index", tags=["api路由"], summary="注册接口")(index)

ApiRouter.post("/login", tags=["api路由"], summary="登陆接口")(login)

# FastAPI中两种Redis的使用方式
ApiRouter.get("/test/my/redis", tags=["api路由"], summary="fastapi的state方式")(test_my_redis)

ApiRouter.get("/test/my/redis/depends", tags=["api路由"], summary="依赖注入方式")(test_my_redis_depends)

# Jwt, 用户管理
ApiRouter.get("/admin/user/info",
              tags=["用户管理"],
              summary="获取用户信息",
              dependencies=[Security(check_permissions, scopes=["user_info"])]
              )(user_info)

ApiRouter.delete("/admin/user/del",
                 tags=["用户管理"],
                 summary="用户删除",
                 dependencies=[Security(check_permissions, scopes=["user_delete"])]
                 )(user_del)

ApiRouter.post("/admin/user/add",
               tags=["用户管理"],
               summary="用户添加",
               # dependencies=[Security(check_permissions, scopes=["user_add"])]
               )(user_add)

ApiRouter.get("/admin/user/rules",
              tags=["用户管理"],
              summary="查询用户权限",
              # dependencies=[Security(check_permissions, scopes=["user_add"])]
              )(get_user_rules)