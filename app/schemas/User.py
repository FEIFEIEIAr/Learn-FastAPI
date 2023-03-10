"""
schemas模型
"""
from pydantic import Field, BaseModel
from typing import Optional
from app.schemas.Base import BaseResp


class CreateUser(BaseModel):
    username: str = Field(min_length=3, max_length=10)
    password: str = Field(min_length=8, max_length=12)


class AccountLogin(BaseModel):
    account: str = Field(min_length=3, max_length=10)
    password: str = Field(min_length=8, max_length=12)


class UserInfo(BaseModel):
    id: int
    username: str
    age: Optional[int]
    user_type: bool
    nickname: Optional[str]
    user_phone: Optional[str]
    user_email: Optional[str]
    full_name: Optional[str]
    user_status: bool
    header_img: Optional[str]
    sex: int


class CurrentUser(BaseResp):
    data: UserInfo


class AccessToken(BaseModel):
    token: Optional[str]
    expires_in: Optional[int]


class UserLogin(BaseResp):
    data: AccessToken