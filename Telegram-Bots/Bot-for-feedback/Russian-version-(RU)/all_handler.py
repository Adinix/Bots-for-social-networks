from dp_bot import dp, bot
from config import chat_bot_communication as id_com
from aiogram import Dispatcher
from aiogram.types import ParseMode, Message
from aiogram.utils.exceptions import BotBlocked
import db


# Обработчик команды /start
@dp.message_handler(commands='start')
async def start(msg: Message):
    # Проверяем, что сообщение пришло из личного чата (не из группы или канала)
    if msg.chat.id > 0:
        user_id = msg.from_user.id
        # Получаем информацию о пользователе из базы данных
        one_start = await db.get_chat_info(user_id)

        # Если пользователя нет в базе или у него еще нет настроек start_command
        if not one_start or one_start[0][1] == 0:
            # Отправляем приветственное сообщение и добавляем пользователя в базу с настройкой start_command = 1
            if msg.from_user.first_name:
                await msg.answer(text=f"<b>Отправьте первое сообщение {msg.from_user.first_name} чтобы начать общаться</b>", parse_mode=ParseMode.HTML)
            elif msg.from_user.username:
                await msg.answer(text=f"<b>Отправьте первое сообщение @{msg.from_user.username} чтобы начать общаться</b>", parse_mode=ParseMode.HTML)
            else:
                await msg.answer(text=f"<b>Отправьте первое сообщение чтобы начать общаться</b>", parse_mode=ParseMode.HTML)

            await db.insert_settings(user_id, 1)
        else:
            # Если у пользователя уже есть настройка start_command, отправляем информацию о нем в чат id_com
            await bot.send_message(chat_id=id_com,
                                    parse_mode=ParseMode.HTML,
                                    text=f"Имя: {msg.from_user.first_name}\n" +
                                        f"Фамилия: {msg.from_user.last_name}\n" +
                                        f"User name: @{msg.from_user.username}\n" +
                                        f"ID: {msg.from_user.id}\n\n" +
                                        f"/start")
    else:
        if msg.chat.id != id_com:
        # Отвечаем, если команда /start была отправлена не из личного чата
            await msg.answer(text="❗️ Я переписываюсь только в лс!\nПросто меня смущает много народу❗️")


# Обработчик команды /chat_info
@dp.message_handler(commands="chat_info")
async def chat_info(msg: Message):
    if msg.chat.id < 0:
        # Отправляем информацию о пользователе и чате, из которого пришла команда /chat_info
        await msg.answer(f"USER-INFO = {msg.from_user}\n\nCHAT-INFO = {msg.chat}")


# Обработчик ответных сообщений на файлы и обычные сообщения
@dp.message_handler(content_types=['document', 'audio', 'photo', 'video', 'voice', 'sticker'], is_reply=True)
async def handle_reply_files_and_text(msg: Message):
    if msg.chat.id != id_com:
        if msg.chat.id > 0:
            reply_user_info = f"Имя: {msg.from_user.first_name}\n" \
                                f"Фамилия: {msg.from_user.last_name}\n" \
                                f"User name: @{msg.from_user.username}\n" \
                                f"ID: {msg.from_user.id}\n\n" \
                                f"{msg.text or msg.caption or msg.caption or ''}"

            if msg.document:
                await bot.send_document(chat_id=id_com, document=msg.document.file_id, caption=reply_user_info)
            elif msg.audio:
                await bot.send_audio(chat_id=id_com, audio=msg.audio.file_id, caption=reply_user_info)
            elif msg.photo:
                await bot.send_photo(chat_id=id_com, photo=msg.photo[-1].file_id, caption=reply_user_info)
            elif msg.video:
                await bot.send_video(chat_id=id_com, video=msg.video.file_id, caption=reply_user_info)
            elif msg.voice:
                await bot.send_voice(chat_id=id_com, voice=msg.voice.file_id, caption=reply_user_info)
            elif msg.sticker:
                await bot.send_sticker(chat_id=id_com, data=msg.sticker.file_id)
        else:
            await msg.answer(text="❗️ Я переписываюсь только в лс!\nЕсли интересно по чему, то из-за того что меня смущает много народу)")
    else:
        try:
            try:
                # Получаем информацию о пользователе, на чье сообщение был дан ответ, и отправляем ему ответ
                user_info = msg.reply_to_message.text.split("\n")
                user_id = user_info[3].replace("ID: ", "")

                msg_text = f"{msg.text or msg.caption or msg.caption or ''}"

                if msg.document:
                    await bot.send_document(chat_id=user_id, document=msg.document.file_id, caption=msg_text)
                elif msg.audio:
                    await bot.send_audio(chat_id=user_id, audio=msg.audio.file_id, caption=msg_text)
                elif msg.photo:
                    await bot.send_photo(chat_id=user_id, photo=msg.photo[-1].file_id, caption=msg_text)
                elif msg.video:
                    await bot.send_video(chat_id=user_id, video=msg.video.file_id, caption=msg_text)
                elif msg.voice:
                    await bot.send_voice(chat_id=user_id, voice=msg.voice.file_id, caption=msg_text)
                elif msg.sticker:
                    await bot.send_sticker(chat_id=user_id, data=msg.sticker.file_id)

            except BotBlocked:
                # Если пользователь заблокировал бота, отправляем уведомление в чат id_com
                await msg.answer(parse_mode=ParseMode.HTML, text=f"<b>Этот пользователь заблокировал бота!</b>")
        except IndexError:
            pass


@dp.message_handler(content_types=['text'], is_reply=True)
async def handle_all_reply_message(msg: Message):
    if msg.chat.id != id_com:
        if msg.chat.id > 0:
            # Отправляем информацию о пользователе и его ответное сообщение в чат id_com
            await bot.send_message(chat_id=id_com,
                                    parse_mode=ParseMode.HTML,
                                    text=f"Имя: {msg.from_user.first_name}\n" +
                                        f"Фамилия: {msg.from_user.last_name}\n" +
                                        f"User name: @{msg.from_user.username}\n" +
                                        f"ID: {msg.from_user.id}\n\n" +
                                        f"{msg.text}")
        else:
            # Отвечаем, если ответное сообщение было отправлено не из личного чата
            await msg.answer(text="❗️ Я переписываюсь только в лс!\nЕсли интересно по чему, то из-за того что меня смущает много народу)")
    else:
        try:
            try:
                # Получаем информацию о пользователе, на чье сообщение был дан ответ, и отправляем ему ответ
                if msg.reply_to_message and msg.reply_to_message.text:
                    user_info = msg.reply_to_message.text.split("\n")
                    user_id = user_info[3].replace("ID: ", "")
                    await bot.send_message(chat_id=user_id, text=msg.text, parse_mode=ParseMode.HTML)
                else:
                    pass
            except BotBlocked:
                # Если пользователь заблокировал бота, отправляем уведомление в чат id_com
                await msg.answer(parse_mode=ParseMode.HTML, text=f"<b>Этот пользователь заблокировал бота!</b>")
        except IndexError:
            pass


# Обработчик файлов и обычных сообщений
@dp.message_handler(content_types=['document', 'audio', 'photo', 'video', 'voice', 'sticker', 'text'])
async def handle_files_and_text(msg: Message):
    if msg.chat.id > 0:
        if msg.chat.id != id_com:
            user_info = f"Имя: {msg.from_user.first_name}\n" \
                        f"Фамилия: {msg.from_user.last_name}\n" \
                        f"User name: @{msg.from_user.username}\n" \
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
        await msg.answer(text="❗️ Я переписываюсь только в лс!\nЕсли интересно по чему, то из-за того что меня смущает много народу)")


# Регистрация всех обработчиков в объекте dp.Dispatcher
def register_handlers(dp: Dispatcher):
    dp.register_message_handler(start, commands='start')
    dp.register_message_handler(chat_info, commands="chat_info")
    dp.register_message_handler(handle_all_reply_message, content_types=['text'], is_reply=True)
    dp.register_message_handler(handle_reply_files_and_text, content_types=['document', 'audio', 'photo', 'video', 'voice', 'sticker'], is_reply=True)
    dp.register_message_handler(handle_files_and_text, content_types=['document', 'audio', 'photo', 'video', 'voice', 'sticker', 'text'])
