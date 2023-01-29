"""
路由聚合, 聚合API路由和视图路由
"""
from app.api.Base import ApiRouter
from app.views.Base import ViewsRouter
from fastapi import APIRouter


AllRouter = APIRouter()

# 视图路由
AllRouter.include_router(ViewsRouter)
# API路由
AllRouter.include_router(ApiRouter)
