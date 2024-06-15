from src.dependencies.api_key_verification import VerifyAPIKey
from src.schemas.orders import PlacedOrder, get_responses, RequestOrder, OrderRandom
from src.schemas.main import ErrorResponse
from src.database.connection import db_session
from src.services.orders import ServiceOrders
from sqlalchemy.ext.asyncio import AsyncSession
from typing import Union
from fastapi import APIRouter, Depends

orders_route = APIRouter(tags=["order"], dependencies=[Depends(VerifyAPIKey())])


@orders_route.post(
    "/orders",
    description="Place a order",
    responses=get_responses,
    response_model=Union[PlacedOrder, ErrorResponse],
)
async def list_broths(body: RequestOrder, conn: AsyncSession = Depends(db_session)):
    return await ServiceOrders(conn).place_order(body)

@orders_route.post(
    "/orders/generate-id",
    description="Generate a order",
    response_model=Union[OrderRandom, ErrorResponse],
)
async def get_latest_order(conn: AsyncSession = Depends(db_session)):
    return await ServiceOrders(conn).get_latest_order()
