from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from app.db.session import get_session
from app.models.user import User, UserCreate

router = APIRouter()

@router.post("/join", response_model=User)
def create_user(user_create: UserCreate, session: Session = Depends(get_session)):
    user = User(name=user_create.name)
    session.add(user)
    session.commit()
    session.refresh(user)
    return user

@router.get("/{user_num}", response_model=User)
def read_user(user_num: int, session: Session = Depends(get_session)):
    user = session.get(User, user_num)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user