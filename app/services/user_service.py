from fastapi import HTTPException
from sqlmodel import Session, select
from app.schemas.user_schema import JoinRequest, JoinResponse, UpdateRequest, UpdateResponse, LoginRequest, LoginResponse
from app.models.user_model import User
from app.utils.password_utils import hash_password, verify_password
from app.exceptions.validation_exception import ValidationException
from app.exceptions.business_exception import BusinessException

# 회원가입
def create_user(join_request: JoinRequest, session: Session) -> JoinResponse:
    # TODO: Validation 체크

    # ID 중복 체크
    existing_user_by_user_id = session.exec(
        select(User).where(User.user_id == join_request.user_id)
    ).first()

    # 핸드폰번호 중복 체크
    existing_user_by_phone_number = session.exec(
        select(User).where(User.phone_number == join_request.phone_number)
    ).first()

    # 이메일 중복 체크
    existing_user_by_email = session.exec(
        select(User).where(User.email == join_request.email)
    ).first()

    # BusinessException
    errors = {}
    if existing_user_by_user_id:
        errors["user_id"] = "ID 중복"
    if existing_user_by_phone_number:
        errors["phone_number"] = "핸드폰번호 중복"
    if existing_user_by_email:
        errors["email"] = "이메일 중복"
    if errors:
        raise BusinessException(errors)

    user = User(
        user_id=join_request.user_id,
        password=hash_password(join_request.password),
        name=join_request.name,
        phone_number=join_request.phone_number,
        email=join_request.email
    )

    session.add(user)
    session.commit()
    session.refresh(user)

    return JoinResponse(message="회원가입 성공")

def read_user_by_user_num(user_num: int, session: Session) -> User:
    # TODO: Validation 체크

    user = session.get(User, user_num)

    # BusinessException
    errors = {}
    if not user:
        errors = "존재하지 않는 사용자입니다."
    if errors:
        raise BusinessException(errors)

    return user

def update_user_by_user_num(user_num: int, update_request: UpdateRequest, session: Session) -> UpdateResponse:
    # TODO: Validation 체크 (내 정보랑 input정보 비교)

    user = session.get(User, user_num)

    # BusinessException
    errors = {}
    if not user:
        errors = "존재하지 않는 사용자입니다."
    if errors:
        raise BusinessException(errors)

    if update_request.user_id or update_request.phone_number or update_request.email:
        # ID 중복 체크
        existing_user_by_user_id = session.exec(
            select(User).where(User.user_id == update_request.user_id, User.user_num != user_num)
        ).first()

        # 핸드폰번호 중복 체크
        existing_user_by_phone_number = session.exec(
            select(User).where(User.phone_number == update_request.phone_number, User.user_num != user_num)
        ).first()

        # 이메일 중복 체크
        existing_user_by_email = session.exec(
            select(User).where(User.email == update_request.email, User.user_num != user_num)
        ).first()

        # BusinessException
        errors = {}
        if existing_user_by_user_id:
            errors["user_id"] = "ID 이미 존재"
        if existing_user_by_phone_number:
            errors["phone_number"] = "핸드폰번호 이미 존재"
        if existing_user_by_email:
            errors["email"] = "이메일 이미 존재"
        if errors:
            raise BusinessException(errors)

    # 입력된 데이터만 Update
    update_data = update_request.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(user, key, value)

    session.add(user)
    session.commit()
    session.refresh(user)

    return UpdateResponse(message="회원정보 수정 성공")

def login_user(login_request: LoginRequest, session: Session) -> LoginResponse:
    # TODO: 토큰 기반 로그인

    user = session.exec(
        select(User).where(User.user_id == login_request.user_id)
    ).first()

    # BusinessException
    errors = {}
    if not user:
        errors = "존재하지 않는 사용자입니다."
    elif not verify_password(login_request.password, user.password):
        errors = "비밀번호가 일치하지 않습니다."
    if errors:
        raise BusinessException(errors)

    return LoginResponse(message="로그인 성공")