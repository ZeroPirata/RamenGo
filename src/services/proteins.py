from sqlalchemy.ext.asyncio import AsyncSession
from src.models.proteins import ModelProteins

class ServiceProteins:
    def __init__(self, connection: AsyncSession) -> None:
        self._conn = connection
        self._proteins = ModelProteins()

    def fetch_all_proteins(self):
        return self._proteins.get_all_proteins(self._conn)
