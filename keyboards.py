from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram import types

inline_kb = types.ReplyKeyboardMarkup(
    keyboard=[
            [
                types.KeyboardButton(text='💡 Adilet'),
                types.KeyboardButton(text='🏞 Sayan'),
            ],
            [
                types.KeyboardButton(text='💡 Laura'),
                types.KeyboardButton(text='🏞 Muhammad'),
            ],
        ],
        resize_keyboard=True,
)

confirm_keyboard = types.InlineKeyboardMarkup(inline_keyboard=[
        [
            types.InlineKeyboardButton(text="Да", callback_data="confirm_send_email"),
            types.InlineKeyboardButton(text="Отмена", callback_data="cancel_send_email")
        ]
    ])