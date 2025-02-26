import asyncio
import os

from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart, Command
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("TOKEN")

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def start(message: types.Message):
    await message.answer("Hello This is your first bot !!!")


@dp.message(Command("help"))
async def help_(message: types.Message):
    await message.answer("You asked help???")


@dp.message()
async def echo(message: types.Message):
    if message.sticker:
            await message.answer(f"{message.sticker.file_id}")
    if message.text == "adilet":
        await message.answer("🎵🎵🎵Это черный пистолет ХЕЙ🎵🎵🎵🎵"
                             "🎵🎵🎵Это черный пистолет ХЕЙ🎵🎵🎵🎵")
    elif message.text == "sayan" or message.text == "laura":
        await message.answer_sticker("CAACAgIAAxkBAANlZ7xdQWDZ81rjY5RQ698ZO_nSvEYAAikAAwzfKCydkWe2NO6C9TYE")
    elif message.text == "muhammad":
        await message.answer_sticker("CAACAgIAAxkBAANEZ7xbsCWHc5rtPTJT8Sr-VjpUW6UAAj4AAwzfKCycoDBeXCS3DzYE")
    else:
        await message.answer(f"You typed {message.text}")



async def main():
    print("Bot started...")
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())