from aiogram import Router, F, types
from database.db import AsyncSessionLocal
from database.models import User
from sqlalchemy import select

router = Router()

# --- ТВОИ ПРЕДЫДУЩИЕ КНОПКИ ---

@router.message(F.text.contains("Офферы"))
async def process_offers(message: types.Message):
    await message.answer("🔥 **Список офферов Grip Team из БД:**\n\nСкоро выгрузим сюда актуальные офферы!")

@router.message(F.text.contains("цифры"))
async def process_stats(message: types.Message):
    await message.answer("📈 **Твоя статистика за сегодня:**\n\nПросмотры: 0\nПереходы: 0\nЛиды: 0")

@router.message(F.text.contains("История"))
async def process_history(message: types.Message):
    await message.answer("📁 **История твоих заявок:**\n\nПока тут пусто.")


# --- ДОБАВЛЯЕМ НОВЫЕ КНОПКИ ---

# Ловим кнопку "💸 Подача на оплату"
@router.message(F.text.contains("оплату"))
async def process_payout(message: types.Message):
    await message.answer(
        "💸 **Заявка на выплату**\n\n"
        "Чтобы подать заявку на выплату, у тебя должен быть закрыт минимальный холд.\n"
        "Введи сумму для вывода и реквизиты (USDT TRC-20 / Карта):\n\n"
        "_(Здесь позже мы настроим пошаговый сбор данных через FSM-состояния)_"
    )

# Ловим кнопку "👤 Профиль"
@router.message(F.text.contains("Профиль"))
async def process_profile(message: types.Message):
    # Давай сразу сделаем красивый вывод профиля воркера
    user_id = message.from_user.id
    username = message.from_user.username or "не указан"
    full_name = message.from_user.full_name

    await message.answer(
        f"👤 **Твой профиль в Grip Team**\n\n"
        f"├ ID: `{user_id}`\n"
        f"├ Имя: {full_name}\n"
        f"├ Telegram: @{username}\n"
        f"└ Статус: Воркер\n\n"
        f"💰 **Баланс:** 0.00 $\n"
        f"⏱ **В холде:** 0.00 $"
    )