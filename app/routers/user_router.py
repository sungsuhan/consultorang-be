from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from app.db.session import get_session
from app.models.user_model import User, UserJoin, UserUpdate
from app.services.user_service import create_user, read_user_by_user_num, update_user_by_user_num

router = APIRouter()

@router.post("/join", response_model=User)
def join(user_join: UserJoin, session: Session = Depends(get_session)):
    return create_user(user_join, session)

@router.get("/{user_num}", response_model=User)
def get_user_info(user_num: int, session: Session = Depends(get_session)):
    return read_user_by_user_num(user_num, session)

@router.patch("/{user_num}", response_model=User)
def update_user_info(
    user_num: int,
    user_update: UserUpdate,
    session: Session = Depends(get_session)
):
    return update_user_by_user_num(user_num, user_update, session)