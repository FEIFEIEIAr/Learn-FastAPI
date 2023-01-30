"""
home页面视图
"""
from typing import Optional

from fastapi import Request, Cookie


async def home(request: Request, session_id: Optional[str] = Cookie(None)):
    # return request.app.state.views.TemplateResponse("index.html", {"request": request, "id": id})
    cookie = session_id
    session = request.session.get("session")
    page_data = {
        "cookie": cookie,
        "session": session
    }
    # request.session.setdefault("55555", "hdaldais")
    return request.app.state.views.TemplateResponse("index.html", {"request": request, **page_data})
