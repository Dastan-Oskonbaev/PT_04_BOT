from aiogram import types

start_kb = types.ReplyKeyboardMarkup(
    keyboard=[
            [
                types.KeyboardButton(text='💡 Список учеников'),
                types.KeyboardButton(text='🏞 Расписание'),
            ],
            [
                types.KeyboardButton(text='💡 Оценки за четверть по предметам'),
                types.KeyboardButton(text='🏞 Предметы и темы'),
            ],
            [
                types.KeyboardButton(text='Дополнительная информация')
            ]
        ],
        resize_keyboard=True,
)

confirm_keyboard = types.InlineKeyboardMarkup(inline_keyboard=[
        [
            types.InlineKeyboardButton(text="Да", callback_data="confirm_send_email"),
            types.InlineKeyboardButton(text="Отмена", callback_data="cancel_send_email")
        ]
    ])