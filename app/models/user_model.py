from typing import Optional

from sqlmodel import SQLModel, Field

# 공통 필드
class UserBase(SQLModel):
    pass

# 회원 가입
class UserJoin(UserBase):
    user_id: str
    name: str

# 회원 정보 수정
class UserUpdate(UserBase):
    user_id: Optional[str] = None # 업데이트는 부분 가능하므로 Optional
    name: Optional[str] = None  # 업데이트는 부분 가능하므로 Optional

# user 테이블 모델
class User(UserBase, table=True):
    user_num: Optional[int] = Field(default=None, primary_key=True)
    user_id: str
    name: str