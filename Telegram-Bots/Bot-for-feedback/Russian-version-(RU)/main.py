from dp_bot import dp
from aiogram.utils import executor
from config import timer
import asyncio
import db


async def on_startup(dp):
    """
    Функция, которая будет вызвана при старте бота.
    """
    await db.connect_db_user()
    asyncio.create_task(reset_start_command_timer())
    print('Bot Start!')


# Подключаем хендлеры
import all_handler

all_handler.register_handlers(dp)


async def reset_start_command_timer():
    """
    Функция для периодического сброса значения start_command в базе данных каждые timer секунд.

    Эта функция вызывает саму себя после ожидания timer секунд, чтобы создать периодическую задачу.
    """
    await db.update_all_settings(0)

    await asyncio.sleep(timer) 

    await reset_start_command_timer()
    asyncio.create_task(reset_start_command_timer())


# Запускаем бота
if __name__ == '__main__':
    executor.start_polling(
        dp,
        skip_updates=True,
        on_startup=on_startup
    )
