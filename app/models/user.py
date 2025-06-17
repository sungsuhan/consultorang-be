from typing import Optional

from sqlmodel import SQLModel, Field

# 공통 필드
class UserBase(SQLModel):
    name: str

# 회원 가입
class UserCreate(UserBase):
    pass

# user 테이블 모델
class User(UserBase, table=True):
    user_num: Optional[int] = Field(default=None, primary_key=True)