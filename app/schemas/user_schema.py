from typing import Optional

from pydantic import BaseModel


# 회원가입
class JoinRequest(BaseModel):
    user_id: str
    password: str
    name: str
    phone_number: str
    email: str

class JoinResponse(BaseModel):
    message: str

# 회원정보수정
class UpdateRequest(BaseModel):
    user_id: Optional[str] = None
    password: Optional[str] = None
    name: Optional[str] = None
    phone_number: Optional[str] = None
    email: Optional[str] = None

class UpdateResponse(BaseModel):
    message: str

# 회원탈퇴
class WithdrawRequest(BaseModel):
    user_id: str
    password: str

class WithdrawResponse(BaseModel):
    message: str

# 로그인
class LoginRequest(BaseModel):
    user_id: str
    password: str

class LoginResponse(BaseModel):
    message: str # TODO: 토큰, user_num 등...
