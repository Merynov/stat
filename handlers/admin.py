from aiogram import Router, types
from aiogram.filters import CommandStart
from database.db import AsyncSessionLocal
from database.models import User
from sqlalchemy import select

# Создаем роутер, который мы потом импортировали в main.py
router = Router()

@router.message(CommandStart())
async def cmd_start(message: types.Message):
    # Самый простой текстовый ответ для проверки связи
    await message.answer(
        f"Привет, {message.from_user.full_name}!\n"
        f"Бот успешно связался с базой данных `cpa_db` и готов к работе. 🚀"
    )