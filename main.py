import asyncio
import logging
from aiogram import Bot, Dispatcher
from config_data.config import config
from database.db import init_db

logger = logging.getLogger(__name__)


async def main():
    logging.basicConfig(level=logging.INFO)

    await init_db()
    logger.info("База данных успешно инициализирована")

    bot = Bot(token=config.bot_token.get_secret_value())
    dp = Dispatcher()


    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())