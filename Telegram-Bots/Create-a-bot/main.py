import asyncio
from bot_instance import bot, dp 
from os import getenv
import logging
import sys
from data_base import db
from handlers import all_handler, FSM



# ! Запускается при старте
async def on_startup(dispatcher):
    await db.connect_db_user()
    print('Bot Start!')


# Запуск бота
async def main():

    global dp, bot

    dp.startup.register(on_startup)

    dp.include_routers(FSM.router)
    dp.include_routers(all_handler.router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())



if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())