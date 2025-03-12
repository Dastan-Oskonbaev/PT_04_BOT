from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram import types

inline_kb = types.ReplyKeyboardMarkup(
    keyboard=[
            [
                types.KeyboardButton(text='💡 Картинка'),
                types.KeyboardButton(text='🏞 Погода'),
            ],
            [
                types.KeyboardButton(text='💡 Курс валют'),
                types.KeyboardButton(text='🏞 Список фильмов'),
            ],
            [
                types.KeyboardButton(text='💡 Шутка'),
                types.KeyboardButton(text='🏞 Пройти опрос'),
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