from dotenv import load_dotenv
import os
from aiogram import Bot, Dispatcher, executor, types

load_dotenv()
bot = os.getenv("BOT_TOKEN")
