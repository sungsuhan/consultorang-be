from app.exceptions.base_exception import BaseException
from fastapi import status as http_status


class ValidationException(BaseException):
    def __init__(self, errors: dict):
        super().__init__(errors, status_code=http_status.HTTP_400_BAD_REQUEST)