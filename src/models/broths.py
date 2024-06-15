from typing import List
from src.database.orm import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import BigInteger, Integer, String, text
from sqlalchemy.ext.asyncio import AsyncSession
from src.schemas.broths import Broths
from src.logger import LOGGER


class ModelBroth(Base):
    __tablename__ = "broths"

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    price: Mapped[int] = mapped_column(Integer, nullable=False)
    imageInactive: Mapped[str] = mapped_column(String, nullable=True, default="https://example.com/inactive.svg")
    imageActive: Mapped[str] = mapped_column(String, nullable=True, default="https://example.com/active.svg")
    description: Mapped[str] = mapped_column(String, nullable=True)

    orders: Mapped[List["ModelOrders"]] = relationship("ModelOrders", back_populates="broth")  # type: ignore # noqa: F821

    async def get_all_broths(self, conn: AsyncSession) -> List[Broths]:
        try:
            async with conn.begin() as exec:
                exec = exec.session
                query = text("SELECT * FROM broths")
                result = await exec.execute(query)
                broths = result.fetchall()
                columns = result.keys()
                broths_list = []
                for row in broths:
                    broth_dict = dict(zip(columns, row))
                    broths_list.append(broth_dict)
                return broths_list
        except Exception as e:
            LOGGER.error("[ModelBroth - get_all_broths] Failed to return all proteins")
            LOGGER.error(repr(e))
            raise e

    async def get_broth(self, conn: AsyncSession, brothId: int) -> Broths:
        try:
            async with conn.begin() as exec:
                exec = exec.session
                query = text("SELECT * FROM broths WHERE id = :brothId")
                result = await exec.execute(query, {"brothId": brothId})
                broth = result.fetchone()
                if broth:
                    return broth._asdict()
        except Exception as e:
            LOGGER.error("[ModelBroth - get_broth] Failed to return broth by id")
            LOGGER.error(repr(e))
            raise e
