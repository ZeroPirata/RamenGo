from src.middleware.exception import CustomHTTPException
from src.models.orders import ModelOrders
from src.models.proteins import ModelProteins
from src.models.broths import ModelBroth
from src.schemas.orders import RequestOrder, PlacedOrder, OrderRandom
from src.logger import LOGGER
from sqlalchemy.ext.asyncio import AsyncSession


class ServiceOrders:
    def __init__(self, connection: AsyncSession) -> None:
        self._conn = connection
        self._orders = ModelOrders()
        self._proteins = ModelProteins()
        self._broths = ModelBroth()

    async def place_order(self, body: RequestOrder) -> PlacedOrder :
        try:
            if body.brothId is None or body.proteinId is None:
                raise CustomHTTPException(403, "both brothId and proteinId are required")
            protein = await self._proteins.get_protein(self._conn, body.proteinId)
            broth = await self._broths.get_broth(self._conn, body.brothId)

            values = {"protein": protein, "broth": broth}
            result = await self._orders.insert_request(self._conn, values) 
            return result
        except Exception as e:
            LOGGER.error("[ServiceOrders - place_order]")
            LOGGER.error(e)
            raise CustomHTTPException(500, "could not place order")

    async def get_latest_order(self) -> OrderRandom:
        return await self._orders.get_order(self._conn)