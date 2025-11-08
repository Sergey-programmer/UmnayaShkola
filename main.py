from dotenv import load_dotenv
import os
from aiogram import Bot, Dispatcher, executor, types

load_dotenv()
bot = Bot(os.getenv("BOT_TOKEN"))
dp = Dispatcher(bot)

@dp.message_handler(commands=["start"])
async def start(message: types.Message):
  await message.answer("Всё работает!")

executor.start_polling(dp)
