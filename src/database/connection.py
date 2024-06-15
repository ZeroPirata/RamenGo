from typing import AsyncGenerator
from fastapi import Depends
from src.config.settings import settings
from src.database.session import DatabaseSessionManager, db_manager
from sqlalchemy.ext.asyncio import AsyncSession


async def init_db():
    await db_manager.init(settings.DATABASE_URI)


async def finish_db():
    await db_manager.close()


def db_conn() -> DatabaseSessionManager:
    return db_manager


async def db_session(manager=Depends(db_conn)) -> AsyncGenerator[AsyncSession, None]:
    async with manager.session() as session:
        yield session
