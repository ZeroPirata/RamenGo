from fastapi.security import APIKeyHeader
from src.middleware.exception import CustomHTTPException
from src.config.settings import settings
from fastapi import Security

class VerifyAPIKey:
    def __init__(self, header_value: str = settings.X_API_KEY):
        self.header_value = header_value

    async def __call__(self, api_key: str = Security(APIKeyHeader(name="x-api-key", auto_error=False))):
        if api_key != self.header_value:
            raise CustomHTTPException(status_code=403, detail="x-api-key header missing")
