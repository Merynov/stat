from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from config_data.config import config
from database.base import Base

engine = create_async_engine(
    config.database_url_asyncpg,  # Твой динамический URL (магия Pydantic)
    echo=False
)

AsyncSessionLocal = async_sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False
)


async def init_db():
    # Прячем импорт внутрь функции, чтобы разорвать циклический импорт!
    from database.models import User, Offer

    async with engine.begin() as conn:
        # Теперь Base.metadata гарантированно знает про User и Offer
        await conn.run_sync(Base.metadata.create_all)