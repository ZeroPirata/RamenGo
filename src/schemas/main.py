from typing import Any, Dict

from pydantic import BaseModel

response_403: Dict[str, Any] = {
    "description": "Forbidden",
    "content": {"application/json": {"example": {"error": "x-api-key header missing"}}},
}

response_500: Dict[str, Any] = {
    "description": "Internal server error",
    "content": {"application/json": {"example": {"error": "could not place order"}}},
}


class ErrorResponse(BaseModel):
    error: str
