from fastapi import FastAPI
from app.routers import user_router
from app.exceptions.base_exception import BaseException, base_exception_handler

app = FastAPI()

app.include_router(user_router.router, prefix="/user", tags=["User"])

app.add_exception_handler(BaseException, base_exception_handler)