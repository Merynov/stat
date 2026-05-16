import asyncio
from logging.config import fileConfig

from sqlalchemy import pool
from sqlalchemy.ext.asyncio import create_async_engine

# Вот правильный импорт контекста:
from alembic import context

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from config_data.config import config as bot_config
from database.base import Base
from database.models import User, Offer

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from config_data.config import config as bot_config
from database.base import Base
# -----------------------------------

config = context.config

if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# Меняем None на метаданные твоей базы данных
target_metadata = Base.metadata

def run_migrations_offline() -> None:
    # Для офлайн-режима берем URL из нашего конфига Pydantic
    url = bot_config.database_url_asyncpg
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()

def do_run_migrations(connection):
    context.configure(connection=connection, target_metadata=target_metadata)

    with context.begin_transaction():
        context.run_migrations()

async def run_async_migrations() -> None:
    # Вместо дефолтного async_engine_from_config создаем асинхронный движок напрямую
    # из строки подключения нашего Pydantic-конфига
    connectable = create_async_engine(
        bot_config.database_url_asyncpg,
        poolclass=pool.NullPool,
    )

    async with connectable.connect() as connection:
        await connection.run_sync(do_run_migrations)

    await connectable.dispose()

def run_migrations_online() -> None:
    asyncio.run(run_async_migrations())

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()