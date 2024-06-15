from typing import Any, Dict
from pydantic import BaseModel
from src.schemas.main import response_403


class Proteins(BaseModel):
    id: int
    name: str
    price: int
    imageInactive: str
    imageActive: str
    description: str


response_200: Dict[str, Any] = {
    "description": "A list of proteins",
    "content": {
        "application/json": {
            "example": [
                {
                    "id": "1",
                    "imageInactive": "https://tech.redventures.com.br/icons/pork/inactive.svg",
                    "imageActive": "https://tech.redventures.com.br/icons/pork/active.svg",
                    "name": "Chasu",
                    "description": "A sliced flavourful pork meat with a selection of season vegetables.",
                    "price": 10,
                }
            ]
        }
    },
}

get_responses: Dict[int, Dict[str, Any]] = {
    200: response_200,
    403: response_403,
}
