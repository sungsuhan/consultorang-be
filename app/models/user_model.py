from typing import Optional

from datetime import datetime
from sqlmodel import SQLModel, Field


# USER 테이블 모델
class User(SQLModel, table=True):
    user_num: Optional[int] = Field(default=None, primary_key=True)
    user_id: str
    password: str
    refresh_token: str
    name: str
    phone_number: str
    email: str
    role: str
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)