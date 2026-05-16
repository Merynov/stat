import asyncio

from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties

from config_data.config import config
from handlers import user_menu, user_offers, admin, channel_events
from middlewares.db_middleware import DbSessionMiddleware


async def main():
    bot = Bot(
        token=config.BOT_TOKEN,
        default=DefaultBotProperties(parse_mode=ParseMode.HTML),
    )

    dp = Dispatcher()

    dp.update.middleware(DbSessionMiddleware())

    dp.include_router(user_menu.router)
    dp.include_router(user_offers.router)
    dp.include_router(admin.router)
    dp.include_router(channel_events.router)

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
