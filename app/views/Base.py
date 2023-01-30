"""
视图路由
"""
from fastapi import APIRouter
from starlette.responses import HTMLResponse

from app.views.Home import home
from app.views.Registration import registration_page, registration_result_page


ViewsRouter = APIRouter()

ViewsRouter.get("/", response_class=HTMLResponse)(home)
ViewsRouter.get("/home", response_class=HTMLResponse)(home)
ViewsRouter.get("/registration", response_class=HTMLResponse)(registration_page)
ViewsRouter.post("/registration/result", response_class=HTMLResponse)(registration_result_page)

# @ViewsRouter.get("/items/{id}", response_class=HTMLResponse)
# async def read_item():
#     # return templates.get_template("index.html").render({"request": request, "id": id})
#     # print(request.app.state.views)