from src.dependencies.api_key_verification import CustomHTTPException
from fastapi import Request, FastAPI
from fastapi.responses import JSONResponse



def define_error_handlers(app: FastAPI):
    @app.exception_handler(CustomHTTPException)
    async def custom_http_exception_handler(request: Request, exc: CustomHTTPException):
        return JSONResponse(status_code=exc.status_code, content=exc.detail)