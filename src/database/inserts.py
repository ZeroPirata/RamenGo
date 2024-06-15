import asyncio
import json
from sqlalchemy import select
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from src.models.proteins import ModelProteins
from src.models.broths import ModelBroth
from src.config.settings import settings

DATABASE_URI = str(settings.DATABASE_URI)
engine = create_async_engine(DATABASE_URI, echo=True)

AsyncSessionLocal = sessionmaker(engine, class_=AsyncSession)


async def insert_proteins(file_name: str):
    async with AsyncSessionLocal() as session:
        with open(file_name, "r") as file:
            data = json.load(file)
        async with session.begin():
            for item in data:
                protein_id = int(item["id"])
                existing_protein = await session.execute(
                    select(ModelProteins).where(ModelProteins.id == protein_id)
                )
                existing_protein = existing_protein.scalars().first()
                if existing_protein is None:
                    protein = ModelProteins(
                        id=int(item["id"]),
                        name=item["name"],
                        price=item["price"],
                        imageInactive=item["imageInactive"],
                        imageActive=item["imageActive"],
                        description=item["description"],
                    )
                    session.add(protein)
            await session.commit()


async def insert_broths(file_name: str):
    async with AsyncSessionLocal() as session:
        with open(file_name, "r") as file:
            data = json.load(file)
        async with session.begin():
            for item in data:
                broth_id = int(item["id"])
                existing_broth = await session.execute(
                    select(ModelBroth).where(ModelBroth.id == broth_id)
                )
                existing_broth = existing_broth.scalars().first()
                if existing_broth is None:
                    broth = ModelBroth(
                        id=int(item["id"]),
                        name=item["name"],
                        price=item["price"],
                        imageInactive=item["imageInactive"],
                        imageActive=item["imageActive"],
                        description=item["description"],
                    )
                    session.add(broth)
            await session.commit()


async def main():
    await insert_proteins("src/database/json/proteins.json")
    await insert_broths("src/database/json/broths.json")

if __name__ == "__main__":
    asyncio.run(main())
