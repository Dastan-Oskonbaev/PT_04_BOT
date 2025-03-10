from aiogram.types import Message, FSInputFile
from aiogram.fsm.context import FSMContext

from keyboards import inline_kb, confirm_keyboard
from states import Survey
from db import db

async def survey_text_handler(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await message.answer("Сколько вам лет")
    await state.set_state(Survey.age)


async def survey_age_handler(message: Message, state: FSMContext):
    await state.update_data(age=message.text)
    await message.answer("Какое ваше хобби?")
    await state.set_state(Survey.hobby)


async def survey_hobby_handler(message: Message, state: FSMContext):
    user_id = await db.check_user(message.chat.id)
    data = await state.get_data()
    name = data.get("name")
    age = data.get("age")
    hobby = message.text
    await message.answer(
        f"CONGRATS {name}!\n You are {age} years old!\n Your hobby is {hobby}"
    )
    await db.add_survey_results(user_id['id'], name, age, hobby)
    await state.clear()


async def main_survey_handler(message: Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state == Survey.name:
        await survey_text_handler(message, state)
    elif current_state == Survey.age:
        await survey_age_handler(message, state)
    elif current_state == Survey.hobby:
        await survey_hobby_handler(message, state)


async def text_handler(message: Message):
    if message.text == "💡 Adilet":
        p = FSInputFile("rolex.jpeg")
        await message.answer_photo(p, "🎵🎵🎵Это черный пистолет ХЕЙ🎵🎵🎵🎵"
                                      "🎵🎵🎵Это черный пистолет ХЕЙ🎵🎵🎵🎵")
    elif message.text == "🏞 Sayan" or message.text == "💡 Laura":
        await message.answer_sticker("CAACAgIAAxkBAANlZ7xdQWDZ81rjY5RQ698ZO_nSvEYAAikAAwzfKCydkWe2NO6C9TYE")
    elif message.text == "🏞 Muhammad":
        await message.answer_sticker("CAACAgIAAxkBAANEZ7xbsCWHc5rtPTJT8Sr-VjpUW6UAAj4AAwzfKCycoDBeXCS3DzYE")
    elif message.text == "show_kb":
        await message.answer(
            text=(
                f'🔥 Вы в режиме работы с контрагентами\n\n'
                f'Выберите желаемое действие 👇\n\n'
            ),
            reply_markup=inline_kb)
    elif message.text == "inline_kb":
        await message.answer(
            text="Вы уверены, что хотите отправить этот файл по email?",
            reply_markup=confirm_keyboard
        )
    else:
        await message.answer(f"You typed {message.text}")