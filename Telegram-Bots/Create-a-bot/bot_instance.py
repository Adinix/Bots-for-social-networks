# bot_instance.py
from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from os import getenv

# Создание бота
bot = Bot(token=getenv("TOKEN"))

# Создание диспетчера
dp = Dispatcher(storage=MemoryStorage())
