import sys

from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker
from sqlalchemy.orm import declarative_base
from typing import Generator

from contextlib import asynccontextmanager

from src.config.settings import settings

Base = declarative_base()

def create_engine_and_session():
    try:
        engine = create_async_engine(
            settings.database_url,
            echo=settings.DB_ECHO_LOG,
            future=True,
            pool_pre_ping=True,
        )
    except Exception as e:
        print(e)
        sys.exit()
    else:
        db_session = async_sessionmaker(
            bind=engine, expire_on_commit=False, autoflush=False
        )
        return engine, db_session


async_engine, async_db_session = create_engine_and_session()


async def get_db():
    session: AsyncSession = async_db_session()
    try:
        yield session
    except:
        await session.rollback()
        raise
    finally:
        await session.close()



async def create_table():
    async with async_engine.begin() as conn:
        # await conn.run_sync(Base.metadata.drop_all, checkfirst=True)
        await conn.run_sync(Base.metadata.create_all)


async def close_pooled_connections():
    await async_engine.dispose()
