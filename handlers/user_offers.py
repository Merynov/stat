from aiogram import Router, F, types

router = Router()

@router.message(F.text == "📢 Офферы")
async def process_offers_button(message: types.Message):
    # Тут пока пишем заглушку, но бот уже ответит!
    await message.answer(
        "🔥 **Список доступных офферов Grip Team:**\n\n"
        "1. TikTok Warm-up (CPA)\n"
        "2. Telegram Traffic Redirection\n\n"
        "Скоро здесь будет выгрузка актуальных офферов прямо из базы данных!"
    )