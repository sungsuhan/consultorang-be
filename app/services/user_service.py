from fastapi import HTTPException
from sqlmodel import Session, select
from app.models.user_model import User, UserJoin, UserUpdate

def create_user(user_join: UserJoin, session: Session) -> User:
    # ID 중복 체크
    statement = select(User).where(User.user_id == user_join.user_id)
    existing_user = session.exec(statement).first()

    if existing_user:
        raise HTTPException(status_code=400, detail="이미 존재하는 ID입니다.")

    user = User(user_id=user_join.user_id, name=user_join.name)
    session.add(user)
    session.commit()
    session.refresh(user)
    return user

def read_user_by_user_num(user_num: int, session: Session) -> User:
    user = session.get(User, user_num)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

def update_user_by_user_num(user_num: int, user_update: UserUpdate, session: Session) -> User:
    user = session.get(User, user_num)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    if user_update.user_id:
        existing_user_id = session.exec(
            select(User).where(User.user_id == user_update.user_id)
        ).first()

        if existing_user_id:
            raise HTTPException(status_code=400, detail="Id already in use")

    user_data = user_update.model_dump(exclude_unset=True)

    for key, value in user_data.items():
        setattr(user, key, value)

    session.add(user)
    session.commit()
    session.refresh(user)
    return user