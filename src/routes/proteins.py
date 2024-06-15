from src.database.connection import db_session
from src.dependencies.api_key_verification import VerifyAPIKey
from src.schemas.proteirns import Proteins, get_responses
from src.schemas.main import ErrorResponse
from typing import List, Union
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.services.proteins import ServiceProteins

proteins_route = APIRouter(tags=["protein"], dependencies=[Depends(VerifyAPIKey())])


@proteins_route.get(
    "/proteins",
    description="A list of proteins",
    responses=get_responses,
    response_model=Union[List[Proteins], ErrorResponse],
)
async def list_broths(conn: AsyncSession = Depends(db_session)):
    return await ServiceProteins(conn).fetch_all_proteins()
