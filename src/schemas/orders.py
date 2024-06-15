from typing import Any, Dict
from pydantic import BaseModel
from src.schemas.main import response_403, response_500
from src.schemas.broths import Broths
from src.schemas.proteirns import Proteins

class RequestOrder(BaseModel):
    brothId: int
    proteinId: int

class OrderRandom(BaseModel):
    orderId: str

class CreateRequest(BaseModel):
    protein: Proteins
    broth: Broths

class PlacedOrder(BaseModel):
    id: int
    description: str
    image: str


response_201: Dict[str, Any] = {
    "description": "Order placed successfully",
    "content": {
        "application/json": {
            "example": [
                {
                    "id": "12345",
                    "description": "Salt and Chasu Ramen",
                    "image": "https://tech.redventures.com.br/icons/ramen/ramenChasu.png",
                }
            ]
        }
    },
}

response_400: Dict[str, Any] = {
    "description": "Invalid request",
    "content": {
        "application/json": {
            "example": {"error": "both brothId and proteinId are required"}
        }
    },
}


get_responses: Dict[int, Dict[str, Any]] = {
    201: response_201,
    400: response_400,
    403: response_403,
    500: response_500,
}
