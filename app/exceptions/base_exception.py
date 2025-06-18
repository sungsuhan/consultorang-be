from fastapi.responses import JSONResponse
from fastapi import status as http_status

class BaseException(Exception):
    def __init__(self, errors: dict, status_code: int = http_status.HTTP_400_BAD_REQUEST):
        self.errors = errors
        self.status_code = status_code

def base_exception_handler(request, exc: BaseException):
    return JSONResponse(
        status_code=exc.status_code,
        content={"errors": exc.errors}
    )