from typing import List
from src.database.orm import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import BigInteger, Integer, String, text
from sqlalchemy.ext.asyncio import AsyncSession
from src.logger import LOGGER
from src.schemas.proteirns import Proteins

class ModelProteins(Base):
    __tablename__ = "proteins"

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    price: Mapped[int] = mapped_column(Integer, nullable=False)
    imageInactive: Mapped[str] = mapped_column(String, nullable=True, default="https://example.com/inactive.svg") 
    imageActive: Mapped[str] = mapped_column(String, nullable=True, default="https://example.com/active.svg") 
    description: Mapped[str] = mapped_column(String, nullable=True)

    orders: Mapped[List["ModelOrders"]] = relationship("ModelOrders", back_populates="protein")  # type: ignore # noqa: F821

    async def get_all_proteins(self, conn: AsyncSession) -> List[Proteins]:
        try:
            async with conn.begin() as exec:
                exec = exec.session
                query = text("SELECT * FROM proteins")
                result = await exec.execute(query)
                proteins = result.fetchall()
                columns = result.keys()
                protein_list = []
                for row in proteins:
                    broth_dict = dict(zip(columns, row))
                    protein_list.append(broth_dict)
                return protein_list
        except Exception as e:
            LOGGER.error("[ModelProteins - get_all_proteins] Failed to return all proteins")
            LOGGER.error(repr(e))
            raise e
        
    async def get_protein(self, conn: AsyncSession, proteinId: int) -> Proteins:
        try:
            async with conn.begin() as exec:
                exec = exec.session
                query = text("SELECT * FROM proteins WHERE id = :proteinId")
                result = await exec.execute(query, {"proteinId": proteinId})
                protein = result.fetchone()
                if protein:
                    return protein._asdict()
        except Exception as e:
            LOGGER.error("[ModelProteins - get_protein] Failed to return protein by id")
            LOGGER.error(repr(e))
            raise e
