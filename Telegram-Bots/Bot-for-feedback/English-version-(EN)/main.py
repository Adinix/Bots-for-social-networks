from dp_bot import dp
from aiogram.utils import executor
from config import timer
import asyncio
import db


async def on_startup(dp):
    """
    Function that will be called when the bot starts.
    """
    await db.connect_db_user()
    asyncio.create_task(reset_start_command_timer())
    print('Bot Start!')


# Connect handlers
import all_handler

all_handler.register_handlers(dp)


async def reset_start_command_timer():
    """
    Function to periodically reset the value of start_command in the database every timer seconds.

    This function calls itself after waiting for timer seconds to create a periodic task.
    """
    await db.update_all_settings(0)

    await asyncio.sleep(timer) 

    await reset_start_command_timer()
    asyncio.create_task(reset_start_command_timer())


# Start the bot
if __name__ == '__main__':
    executor.start_polling(
        dp,
        skip_updates=True,
        on_startup=on_startup
    )
