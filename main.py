import asyncio
import logging
from aiogram import Bot, Dispatcher
from config_data.config import config
from database.db import init_db

# Импортируем роутер из папки handlers.
# Если твой файл называется по-другому (например, user.py), поправь имя в конце.
from handlers.admin import router as admin_router

# Если у тебя есть отдельный файл для обычных юзеров, импортируй его так же:
# from handlers.users import router as users_router

logger = logging.getLogger(__name__)


async def main():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )

    # Инициализируем БД
    await init_db()

    # Берем токен из Pydantic settings
    bot = Bot(token=config.bot_token.get_secret_value())
    dp = Dispatcher()

    # КРИТИЧЕСКИ ВАЖНО: Подключаем роутеры, чтобы бот видел хэндлеры!
    dp.include_router(admin_router)
    # dp.include_router(users_router)

    logger.info("База инициализирована. Бот запускает polling...")

    # Запуск бота
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())