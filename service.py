import os

from aiogram.client.session import aiohttp
from aiogram.types import Message, FSInputFile
from aiogram.fsm.context import FSMContext
from dotenv import load_dotenv
from openai import OpenAI

from keyboards import inline_kb, confirm_keyboard
from states import Survey
from db import db

load_dotenv()

OPENAI_API_KEY=os.getenv('OPENAI_API_KEY')
WEATHER_API_KEY=os.getenv('WEATHER_API_KEY')

client = OpenAI(api_key=OPENAI_API_KEY)

async def chat_with_openai(message: Message, prompt):
    try:
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[{"role": "user",
                       "content": message.text
                       },
                      {"role": "system",
                       "content": f"{prompt}"

                       }],
        )
        reply_text = response.choices[0].message.content
        await message.answer(reply_text)
    except Exception as e:
        print(e)


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
    if message.text == "💡 Картинка":
        pass
        # Здесь вы отправляете inline клавиатуру
    elif message.text == "🏞 Погода":
        weather = await get_weather()
        await message.answer(weather)
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
        await message.answer("sdfsd")


async def get_weather():
    url = f"https://api.openweathermap.org/data/2.5/weather?q=Бишкек&appid={WEATHER_API_KEY}&units=metric"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:
                data = await response.json()
                type_ = data["weather"][0]["main"]
                temp_c = data["main"]["temp"]
                feels_like = data["main"]["feels_like"]
                city = data["name"]
                return f"Погода в городе {city}:{type_}\n Температура:{temp_c}\n Чувствуется как:{feels_like}"
            else:
                return f"Произошла ошибка"



