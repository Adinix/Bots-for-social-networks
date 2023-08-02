from dp_bot import dp, bot
from config import chat_bot_communication as id_com
from aiogram import Dispatcher
from aiogram.types import ParseMode, Message
from aiogram.utils.exceptions import BotBlocked
import db


# Handler for the /start command
# @dp.message_handler(commands='start')
async def start(msg: Message):
    # Check if the message came from a private chat (not from a group or channel)
    if msg.chat.id > 0:
        user_id = msg.from_user.id
        # Get information about the user from the database
        one_start = await db.get_chat_info(user_id)

        # If the user is not in the database or has not set the start_command option yet
        if not one_start or one_start[0][1] == 0:
            # Send a welcome message and add the user to the database with start_command = 1
            if msg.from_user.first_name:
                await msg.answer(text=f"<b>Send your first message {msg.from_user.first_name} to start chatting</b>", parse_mode=ParseMode.HTML)
            elif msg.from_user.username:
                await msg.answer(text=f"<b>Send your first message @{msg.from_user.username} to start chatting</b>", parse_mode=ParseMode.HTML)
            else:
                await msg.answer(text="<b>Send your first message to start chatting</b>", parse_mode=ParseMode.HTML)

            await db.insert_settings(user_id, 1)
        else:
            # If the user has already set the start_command option, send information about them to the id_com chat
            await bot.send_message(chat_id=id_com,
                                    parse_mode=ParseMode.HTML,
                                    text=f"First Name: {msg.from_user.first_name}\n" +
                                        f"Last Name: {msg.from_user.last_name}\n" +
                                        f"User Name: @{msg.from_user.username}\n" +
                                        f"ID: {msg.from_user.id}\n\n" +
                                        f"/start")
    else:
        if msg.chat.id != id_com:
            # Respond if the /start command was sent not from a private chat
            await msg.answer(text="❗️ I only chat in private messages!\nI'm just uncomfortable in crowded places ❗️")


# Handler for the /chat_info command
# @dp.message_handler(commands="chat_info")
async def chat_info(msg: Message):
    if msg.chat.id < 0:
        # Send information about the user and the chat from which the /chat_info command was sent
        await msg.answer(f"USER-INFO = {msg.from_user}\n\nCHAT-INFO = {msg.chat}")


# Handler for files and regular messages
@dp.message_handler(content_types=['document', 'audio', 'photo', 'video', 'voice', 'sticker', 'text'])
async def handle_files_and_text(msg: Message):
    if msg.chat.id > 0:
        if msg.chat.id != id_com:
            user_info = f"First Name: {msg.from_user.first_name}\n" \
                        f"Last Name: {msg.from_user.last_name}\n" \
                        f"User Name: @{msg.from_user.username}\n" \
                        f"ID: {msg.from_user.id}\n\n" \
                        f"{msg.text or msg.caption or msg.caption or ''}"
            if msg.text:
                await bot.send_message(chat_id=id_com, text=user_info)
            elif msg.document:
                await bot.send_document(chat_id=id_com, document=msg.document.file_id, caption=user_info)
            elif msg.audio:
                await bot.send_audio(chat_id=id_com, audio=msg.audio.file_id, caption=user_info)
            elif msg.photo:
                await bot.send_photo(chat_id=id_com, photo=msg.photo[-1].file_id, caption=user_info)
            elif msg.video:
                await bot.send_video(chat_id=id_com, video=msg.video.file_id, caption=user_info)
            elif msg.voice:
                await bot.send_voice(chat_id=id_com, voice=msg.voice.file_id, caption=user_info)
            elif msg.sticker:
                await bot.send_sticker(chat_id=id_com, data=msg.sticker.file_id)
    else:
        await msg.answer(text="❗️ I only chat in private messages!\nIf you're curious why, it's because I feel uncomfortable in crowded places)")


# Handler for reply messages with files and regular messages
@dp.message_handler(content_types=['document', 'audio', 'photo', 'video', 'voice', 'sticker', 'text'], is_reply=True)
async def handle_reply_files_and_text(msg: Message):
    if msg.chat.id != id_com:
        if msg.chat.id > 0:
            user_info = msg.reply_to_message.text.split("\n")
            user_id = user_info[3].replace("ID: ", "")
            
            reply_user_info = f"First Name: {msg.from_user.first_name}\n" \
                                f"Last Name: {msg.from_user.last_name}\n" \
                                f"User Name: @{msg.from_user.username}\n" \
                                f"ID: {msg.from_user.id}\n\n" \
                                f"{msg.text or msg.caption or msg.caption or ''}"

            if msg.text:
                await bot.send_message(chat_id=user_id, text=reply_user_info)
            elif msg.document:
                await bot.send_document(chat_id=user_id, document=msg.document.file_id, caption=reply_user_info)
            elif msg.audio:
                await bot.send_audio(chat_id=user_id, audio=msg.audio.file_id, caption=reply_user_info)
            elif msg.photo:
                await bot.send_photo(chat_id=user_id, photo=msg.photo[-1].file_id, caption=reply_user_info)
            elif msg.video:
                await bot.send_video(chat_id=user_id, video=msg.video.file_id, caption=reply_user_info)
            elif msg.voice:
                await bot.send_voice(chat_id=user_id, voice=msg.voice.file_id, caption=reply_user_info)
            elif msg.sticker:
                await bot.send_sticker(chat_id=user_id, data=msg.sticker.file_id)


# Register all handlers in the dp.Dispatcher object
def register_handlers(dp: Dispatcher):
    dp.register_message_handler(start, commands='start')
    dp.register_message_handler(chat_info, commands="chat_info")
    dp.register_message_handler(handle_files_and_text)
    dp.register_message_handler(handle_reply_files_and_text)
