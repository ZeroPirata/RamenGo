from sqlalchemy.ext.asyncio import AsyncSession
from src.models.broths import ModelBroth

class ServiceBroths:
    def __init__(self, connection: AsyncSession) -> None:
        self._conn = connection
        self._broth = ModelBroth()

    async def fetch_all_broths(self):
        return await self._broth.get_all_broths(self._conn)
