from src.dependencies.api_key_verification import VerifyAPIKey
from src.schemas.broths import Broths, get_responses
from src.schemas.main import ErrorResponse
from src.database.connection import db_session
from src.services.broths import ServiceBroths
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List, Union
from fastapi import APIRouter, Depends

broths_route = APIRouter(tags=["broth"], dependencies=[Depends(VerifyAPIKey())])


@broths_route.get(
    "/broths",
    description="A list of broths",
    responses=get_responses,
    response_model=Union[List[Broths], ErrorResponse],
)
async def list_broths(conn: AsyncSession = Depends(db_session)):
    return await ServiceBroths(conn).fetch_all_broths()
