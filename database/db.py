from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession

from config_data.config import config

engine = create_async_engine(config.database_url)

async_session = async_sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False,
)
