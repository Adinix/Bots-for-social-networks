from bot_instance import bot
from aiogram import types
from aiogram.enums import ParseMode
from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from modules.func import get_chat_lang
import keyboards.inline_keyboards as ikb
from asyncio import sleep
from json import load


router = Router()

msg_id_technical_support = dict()


# ! Обращение в техподдержку
class TechnicalSupport(StatesGroup):
    send_message = State()


@router.callback_query(F.data.startswith('send_message_technical_support_'))
async def technical_support_start(call: types.CallbackQuery, state: FSMContext):

    await state.set_state(TechnicalSupport.send_message)
    
    lang = await get_chat_lang(call.message.chat.id)

    await call.answer(text="")

    await state.set_state(TechnicalSupport.send_message)


    if call.data.split("_")[-1] == "h":
        if lang == "en":
            await bot.edit_message_text(chat_id=call.message.chat.id,
                                    message_id=call.message.message_id,
                                    text='📌 We do not respond quickly, but should respond within 24 hours. If you forgot to mention something or want to add something, send another message.\nYou can start writing your appeal:',
                                    reply_markup=ikb.main_or_help_menu_ikb(lang))

        elif lang == "ua":
            await bot.edit_message_text(chat_id=call.message.chat.id,
                                    message_id=call.message.message_id,
                                    text='📌 Ми не швидко відповідаємо, але протягом 24 годин маємо відповісти. Якщо щось забули згадати або хочете дописати, відправте ще одне повідомлення.\nМожете почати писати своє звернення:',
                                    reply_markup=ikb.main_or_help_menu_ikb(lang))

        elif lang == "ru":
            await bot.edit_message_text(chat_id=call.message.chat.id,
                                    message_id=call.message.message_id,
                                    text='📌 Мы не быстро отвечаем, но в течение 24 часов должны ответить. Если что-то забыли упомянуть или хотите дописать, отправьте еще одно сообщение.\nМожете начать писать свое обращение:',
                                    reply_markup=ikb.main_or_help_menu_ikb(lang))


    else:
        if lang == "en":
            await bot.edit_message_text(chat_id=call.message.chat.id,
                                    message_id=call.message.message_id,
                                    text='📌 We do not respond quickly, but should respond within 24 hours. If you forgot to mention something or want to add something, send another message.\nYou can start writing your appeal:',
                                    reply_markup=ikb.main_or_questions_menu_ikb(lang))

        elif lang == "ua":
            await bot.edit_message_text(chat_id=call.message.chat.id,
                                    message_id=call.message.message_id,
                                    text='📌 Ми не швидко відповідаємо, але протягом 24 годин маємо відповісти. Якщо щось забули згадати або хочете дописати, відправте ще одне повідомлення.\nМожете почати писати своє звернення:',
                                    reply_markup=ikb.main_or_questions_menu_ikb(lang))

        elif lang == "ru":
            await bot.edit_message_text(chat_id=call.message.chat.id,
                                    message_id=call.message.message_id,
                                    text='📌 Мы не быстро отвечаем, но в течение 24 часов должны ответить. Если что-то забыли упомянуть или хотите дописать, отправьте еще одно сообщение.\nМожете начать писать свое обращение:',
                                    reply_markup=ikb.main_or_questions_menu_ikb(lang))

    

    global msg_id_technical_support
    msg_id_technical_support[call.message.chat.id] = call.message.message_id

    await sleep(24 * 60 * 60)
    await bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)



@router.message(TechnicalSupport.send_message)
async def send_message_technical_support(msg: types.Message, state: FSMContext):

    global msg_id_technical_support

    lang = await get_chat_lang(msg.chat.id)

    with open("config.json", 'r') as f:
        config = load(f)
    

    await bot.send_message(chat_id=config["technical_support_chat_id"], 
                            text=f"{msg.from_user.id}\n{msg.from_user.first_name}\n\n{msg.text}")

    await msg.delete()

    if lang == "en":
        await bot.edit_message_text(chat_id=msg.chat.id,
                                message_id=msg_id_technical_support[msg.chat.id],
                                text="✉️ Message sent!\n\n<b>Main menu!</b>", 
                                parse_mode=ParseMode.HTML, 
                                reply_markup=ikb.main_menu_ikb(lang))

    elif lang == "ua":
        await bot.edit_message_text(chat_id=msg.chat.id,
                                message_id=msg_id_technical_support[msg.chat.id],
                                text="✉️ Повідомлення відправлено!\n\n<b>Головне меню!</b>", 
                                parse_mode=ParseMode.HTML, 
                                reply_markup=ikb.main_menu_ikb(lang))

    elif lang == "ru":
        await bot.edit_message_text(chat_id=msg.chat.id,
                                message_id=msg_id_technical_support[msg.chat.id],
                                text="✉️ Сообщение отправлено!\n\n<b>Главное меню!</b>", 
                                parse_mode=ParseMode.HTML, 
                                reply_markup=ikb.main_menu_ikb(lang))

    await state.clear()

    await sleep(24 * 60 * 60)
    await bot.delete_message(chat_id=msg.chat.id, message_id=msg.message_id)
