from aiogram import Router, types
from aiogram.filters import CommandStart
# Импортируем твою готовую реплай-клавиатуру
from keyboards.reply import main_menu

router = Router()

@router.message(CommandStart())
async def cmd_start(message: types.Message):
    await message.answer(
        f"Привет, {message.from_user.full_name}!\n"
        f"Добро пожаловать в панель **Grip Team** 🚀\n\n"
        f"Выбери нужный раздел на клавиатуре внизу:",
        reply_markup=main_menu  # Прикрепляем твои Reply-кнопки
    )