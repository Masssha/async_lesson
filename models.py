import os
import asyncpg
import asyncio
# import sys
#
# if sys.platform:
#     asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())


from sqlalchemy import JSON
from sqlalchemy.orm import DeclarativeBase, mapped_column, Mapped
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncAttrs
#
POSTGRES_PASSWORD = os.getenv('POSTGRES_PASSWORD', 'LLllMMmmqwerty654321')
POSTGRES_USER = os.getenv('POSTGRES_USER', 'postgres')
POSTGRES_DB = os.getenv('POSTGRES_DB', 'sw')
POSTGRES_HOST = os.getenv('POSTGRES_HOST', '127.0.0.1')
# POSTGRES_HOST = os.getenv('POSTGRES_HOST', 'localhost')
POSTGRES_PORT = os.getenv('POSTGRES_PORT', '5435')

#
PG_DSN = f'postgresql+asyncpg://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}'
#
engine = create_async_engine(PG_DSN)

Session = async_sessionmaker(engine, expire_on_commit=False)



class Base(DeclarativeBase, AsyncAttrs):
    pass
#
class Swapi(Base):
    __tablename__ = 'swapi_people'

    id: Mapped[int] = mapped_column(primary_key=True)
    JSON: Mapped[dict] = mapped_column(JSON, nullable=True)


async def init_orm():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)





