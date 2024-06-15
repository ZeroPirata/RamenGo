from src.database.orm import Base
from src.models.broths import ModelBroth
from src.models.proteins import ModelProteins
from src.schemas.orders import CreateRequest, PlacedOrder, OrderRandom
from src.logger import LOGGER

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import BigInteger, String, ForeignKey, text
from sqlalchemy.ext.asyncio import AsyncSession

class ModelOrders(Base):
    __tablename__ = "orders"
    __table_args__ = {'extend_existing': True}

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True, autoincrement=True)
    description: Mapped[str] = mapped_column(String, nullable=False)
    image: Mapped[str] = mapped_column(String, nullable=True, default="https://example.com/ramenChasu.png")

    broth: Mapped["ModelBroth"] = relationship("ModelBroth", back_populates="orders")
    brothId: Mapped[int] = mapped_column(BigInteger, ForeignKey("broths.id"))
    
    protein: Mapped["ModelProteins"] = relationship("ModelProteins", back_populates="orders")
    proteinId: Mapped[int] = mapped_column(BigInteger, ForeignKey("proteins.id"))

    async def get_order(self, conn: AsyncSession) -> OrderRandom:
        try:
            async with conn.begin() as exec:
                exec = exec.session
                query = text("""
                    SELECT id
                    FROM orders
                    ORDER BY id DESC
                    LIMIT 1;
                """)
                result = await exec.execute(query)
                order = result.fetchone()
                if order:
                    order = order._asdict()
                    return { "orderId": str(order['id']) }
        except Exception as e:
            LOGGER.error("[ModelOrders - insert_request]")
            LOGGER.error(e)
            raise

    async def insert_request(self, conn: AsyncSession, values: CreateRequest) -> PlacedOrder:
        try:
            desc = f"{values['broth']['name']} and {values['protein']['name']} Ramen"
            order_data = {
                "description": desc,
                "brothId": values['broth']['id'],
                "proteinId": values['protein']['id']
            }
            async with conn.begin() as exec:
                exec = exec.session
                new_order = ModelOrders(
                    description=order_data['description'],
                    brothId=order_data['brothId'],
                    proteinId=order_data['proteinId']
                )
                exec.add(new_order)
                await exec.commit()
                
                return {
                    "id": new_order.id,
                    "description": new_order.description,
                    "image": new_order.image
                }
        except Exception as e:
            await conn.rollback()
            LOGGER.error("[ModelOrders - insert_request]")
            LOGGER.error(e)
            raise