"""
注册页面视图
"""
from fastapi import Request, Form

from app.models.Base import User


async def registration_page(request: Request):
    """
    注册页面
    :param req:
    :return: html
    """
    return request.app.state.views.TemplateResponse("reg_page.html", {"request": request})

async def registration_result_page(request: Request, username: str = Form(...), password: str = Form(...)):
    """
    注册结果页面
    :param password: str
    :param username: str
    :param request:
    :return: html
    """
    get_user = await User().get_or_none(username=username)
    if get_user:
        return request.app.state.views.TemplateResponse("index.html", {"request": request})
    
    add_user = await User().create(username=username, password=password)
    print("插入的自增ID", add_user.pk)
    print("插入的用户名", add_user.username)

    # 获取当前创建的用户
    get_user = await User().get(username=username)

    return request.app.state.views.TemplateResponse(
        "reg_result_page.html", {"request": request, "username": get_user.username, "password": get_user.password})
    # return request.app.state.views.TemplateResponse("reg_result_page.html", {"request": request, "username": username, "password": password})
