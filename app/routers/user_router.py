from fastapi import APIRouter, Depends
from sqlmodel import Session
from app.db.session import get_session
from app.schemas.user_schema import JoinRequest, JoinResponse, UpdateRequest, UpdateResponse, WithdrawRequest, WithdrawResponse, LoginRequest, LoginResponse
from app.models.user_model import User
from app.services.user_service import create_user, login_user, read_user_by_user_num, update_user_by_user_num, delete_user_by_user_num

router = APIRouter()

@router.post("/join", response_model=JoinResponse, summary="회원가입", description="회원 정보를 받아 신규 회원을 등록합니다.")
def join(join_request: JoinRequest, session: Session = Depends(get_session)):
    return create_user(join_request, session)

@router.get("/{user_num}", response_model=User, summary="회원조회", description="회원 번호를 받아 회원을 조회합니다.")
def get_user_info(user_num: int, session: Session = Depends(get_session)):
    return read_user_by_user_num(user_num, session)

@router.patch("/{user_num}", response_model=UpdateResponse, summary="회원정보수정", description="수정 정보를 받아 회원 정보를 수정합니다.")
def update_user_info(user_num: int, update_request: UpdateRequest, session: Session = Depends(get_session)):
    return update_user_by_user_num(user_num, update_request, session)

@router.delete("/{user_num}", response_model=WithdrawResponse, summary="회원탈퇴", description="회원 정보를 받아 회원을 삭제합니다.")
def withdraw_user(user_num: int, withdraw_request: WithdrawRequest, session: Session = Depends(get_session)):
    return delete_user_by_user_num(user_num, withdraw_request, session)

@router.post("/login", response_model=LoginResponse, summary="로그인", description="ID/PW를 받아 로그인을 합니다.")
def login(login_request: LoginRequest, session: Session = Depends(get_session)):
    return login_user(login_request, session)