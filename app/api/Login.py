"""
登陆
"""
from typing import List
from pydantic import BaseModel


class Login(BaseModel):
    username: str
    password: str
    user: List[int]


def index(age: int = 80):
    return {"fun": "/index", "age": age}


def login(data: Login):
    return data