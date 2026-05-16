from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="📢 Офферы")],
        [KeyboardButton(text="📊 Мои цифры")],
        [KeyboardButton(text="📁 История")],
        [KeyboardButton(text="💸 Подача на оплату")],
        [KeyboardButton(text="👤 Профиль")],
    ],
    resize_keyboard=True,
)
