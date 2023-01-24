"""
视图路由
"""
from fastapi import APIRouter
from starlette.responses import HTMLResponse

from app.views.Home import home


ViewsRouter = APIRouter()

ViewsRouter.get("/items/{id}", response_class=HTMLResponse)(home)

# @ViewsRouter.get("/items/{id}", response_class=HTMLResponse)
# async def read_item():
#     # return templates.get_template("index.html").render({"request": request, "id": id})
#     # print(request.app.state.views)