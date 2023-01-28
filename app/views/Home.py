"""
views home
"""
from fastapi import Request, Form

from app.models.Base import User


async def home(request: Request, id: str):
    return request.app.state.views.TemplateResponse("index.html", {"request": request, "id": id})

async def reg_page(req: Request):
    """
    注册页面
    :param req:
    :return: html
    """
    return req.app.state.views.TemplateResponse("reg_page.html", {"request": req})

async def result_page(request: Request, username: str = Form(...), password: str = Form(...)):
    """
    注册结果页面
    :param password: str
    :param username: str
    :param req:
    :return: html
    """
    get_user = await User().get_or_none(username=username)
    if get_user:
        return request.app.state.views.TemplateResponse("index.html", {"request": request, "id": '用户名已存在'})
    
    add_user = await User().create(username=username, password=password)
    print("插入的自增ID", add_user.pk)
    print("插入的用户名", add_user.username)

    # user_list = await User().all().values()
    # # 打印查询结果
    # for user in user_list:
    #     print("用户:{}".format(user.get('username')), user)

    # 获取当前创建的用户
    get_user = await User().get(username=username)

    return request.app.state.views.TemplateResponse(
        "reg_result_page.html", {"request": request, "username": get_user.username, "password": get_user.password})
    # return request.app.state.views.TemplateResponse("reg_result_page.html", {"request": request, "username": username, "password": password})
