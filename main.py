import asyncio
import os

from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import CommandStart, Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from dotenv import load_dotenv

from db import Database
from states import Survey, Product
import service as service

load_dotenv()

TOKEN = os.getenv("TOKEN")

bot = Bot(token=TOKEN)
dp = Dispatcher()

db = Database(
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    database=os.getenv("DB_NAME"),
    host=os.getenv("DB_HOST"),
    port=os.getenv("DB_PORT"),
)

@dp.message(CommandStart())
async def start(message: types.Message):
    await message.answer("Hello This is your first bot !!!")

@dp.callback_query()
async def callback_query_handler(call: types.CallbackQuery):
    if call.data == "confirm_send_email":
        await call.message.answer("Hello This is your second bot !!!", reply_markup=None)


@dp.message(Command('survey'))
async def survey_handler(message: Message, state: FSMContext):
    await message.answer("Как вас зовут?")
    await state.set_state(Survey.name)

@dp.message(Command('create_product'))
async def create_product_handler(message: Message, state: FSMContext):
    await message.answer("Product name?")
    await state.set_state(Product.product_name)


@dp.message(Command("help"))
async def help_(message: types.Message):
    await message.answer("You asked help???")


@dp.message(F.photo)
async def photo_handler(message: types.Message):
    await message.answer("NICE IMAGE")


@dp.message()
async def echo(message: types.Message, state: FSMContext):
    user_tg_id = await db.check_user(message.chat.id)
    if user_tg_id is None:
        await db.add_user(message.chat.id, message.chat.username, message.chat.first_name, message.chat.last_name)
    current_state = await state.get_state()
    if current_state is not None:
        if current_state.startswith("Survey"):
            await service.main_survey_handler(message, state)
        elif current_state.startswith("Product"):
            pass
    else:
        if message.sticker:
                await message.answer(f"{message.sticker.file_id}")
        if message.photo:
            await message.answer("NICE IMAGE 2")
        if message.text:
            await service.text_handler(message)



async def main():
    print("Bot started...")
    await db.connect()
    try:
        await dp.start_polling(bot)
    except Exception as e:
        print(e)
    finally:
        await db.disconnect()


if __name__ == '__main__':
    asyncio.run(main())


####
###