import asyncio
import logging
from aiogram import Bot, Dispatcher
from config_data.config import config
from database.db import init_db

# Импортируем оба роутера в самом верху
from handlers.user_menu import router as user_menu_router
from handlers.admin import router as admin_router

logger = logging.getLogger(__name__)


async def main():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )

    # Инициализация БД
    await init_db()

    bot = Bot(token=config.bot_token.get_secret_value())

    # 1. Создаем диспетчер внутри функции
    dp = Dispatcher()

    # 2. Регистрируем ВСЕ роутеры внутри функции строго ПОСЛЕ создания dp
    dp.include_router(admin_router)
    dp.include_router(user_menu_router)

    logger.info("База инициализирована. Бот запускает polling...")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())