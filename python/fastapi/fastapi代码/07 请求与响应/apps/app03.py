from fastapi import APIRouter
from typing import Union, Optional
from pydantic import BaseModel, Field, validator
from datetime import date
from typing import List

app03 = APIRouter()


class Addr(BaseModel):
    province: str
    city: str


class User(BaseModel):
    # 没有默认值的就是必填参数
    # name: str = Field(regex="^a")
    name: str
    age: int = Field(default=1, gt=0, lt=100)
    birth: Union[date, None] = None
    friends: List[str] = [1,2,3] #这样123会转换成str
    description: Optional[str] = None
    addr: Addr

    @validator("name")
    def name_must_alpha(cls, value):
        assert value.isalpha(), 'name must be alpha'
        return value


class Data(BaseModel):
    data: List[User]


@app03.post("/user")
async def user(user: User):
    # print(user, type(user))
    print(user, type(user.birth))
    # print(user.name, user.birth)
    # print(user.dict())
    return user


@app03.post("/data")
async def data(data: Data):
    return data
