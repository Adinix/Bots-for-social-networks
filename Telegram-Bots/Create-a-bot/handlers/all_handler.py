from bot_instance import bot
from aiogram import types, Router, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.enums import ParseMode
from data_base import db
from modules.func import get_chat_lang
from keyboards.inline_keyboards import lang_ikb, free_games_ikb, order_bot_ikb, woth_bot_ikb, main_menu_ikb, change_language_ikb, main_menu_back_ikb, main_or_questions_menu_ikb, main_or_help_menu_ikb
from asyncio import sleep
from json import load

dict_msg_id = dict()


router = Router()

# ! command start
@router.message(Command(commands='start'))
async def start(msg: types.Message, state: FSMContext):

    await state.clear()

    lang = await get_chat_lang(msg.chat.id)

    if not lang:

        await msg.answer(text="<b>Choose language:</b>",
                            parse_mode=ParseMode.HTML,
                            reply_markup=lang_ikb())

    else:
        
        if lang == "en":
            await msg.answer(text="<b>Main menu!</b>", 
                            parse_mode=ParseMode.HTML, 
                            reply_markup=main_menu_ikb(lang))

        elif lang == "ua":
            await msg.answer(text="<b>Головне меню!</b>", 
                            parse_mode=ParseMode.HTML, 
                            reply_markup=main_menu_ikb(lang))

        elif lang == "ru":
            await msg.answer(text="<b>Главное меню!</b>", 
                            parse_mode=ParseMode.HTML,
                            reply_markup=main_menu_ikb(lang))
    
    await msg.delete()

    await sleep(24 * 60 * 60)
    await bot.delete_message(chat_id=msg.chat.id, message_id=msg.message_id)





@router.callback_query(lambda x: x.data and x.data.startswith("choice_lang"))
async def start_settings(call: types.CallbackQuery):

    lang = call.data.split("_")[-1]


    if call.message.chat.id > 0:
        await db.insert_settings(call.message.chat.id,
                                lang,
                                call.from_user.first_name,
                                call.from_user.last_name,
                                call.from_user.username,
                                call.from_user.language_code,
                                type=call.message.chat.type)

    else:
        if call.message.chat.all_members_are_administrators == True:
            all_members_are_administrators = 1
        else: 
            all_members_are_administrators = 0

        await db.insert_settings(call.message.chat.id,
                                lang, 
                                title=call.message.chat.title, 
                                type=call.message.chat.type, 
                                all_members_are_administrators=all_members_are_administrators)


    if lang == "en":
        await bot.edit_message_text(chat_id=call.message.chat.id, 
        message_id=call.message.message_id, 
        text='🇺🇸 You have chosen English!')

        await start_hello(lang, call.message.chat.id, call.message.from_user.last_name)
        await bot.send_message(chat_id=call.message.chat.id, 
                                text="<b>Main menu!</b>", 
                                parse_mode=ParseMode.HTML, 
                                reply_markup=main_menu_ikb(lang))

    elif lang == "ua":
        await bot.edit_message_text(chat_id=call.message.chat.id, 
        message_id=call.message.message_id, 
        text='🇺🇦 Ви обрали українську мову!')

        await start_hello(lang, call.message.chat.id, call.message.from_user.last_name)
        await bot.send_message(chat_id=call.message.chat.id, 
                                text="<b>Головне меню!</b>", 
                                parse_mode=ParseMode.HTML, 
                                reply_markup=main_menu_ikb(lang))        

    elif lang == "ru":
        await bot.edit_message_text(chat_id=call.message.chat.id, 
        message_id=call.message.message_id, 
        text='🇷🇺 Вы выбрали руский язык!')

        await start_hello(lang, call.message.chat.id, call.message.from_user.last_name)
        await bot.send_message(chat_id=call.message.chat.id, 
                                text="<b>Главное меню!</b>", 
                                parse_mode=ParseMode.HTML, 
                                reply_markup=main_menu_ikb(lang))
        
    await sleep(24 * 60 * 60)
    await bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)



async def start_hello(lang, chat_id, last_name):

    if lang == "en":
        await bot.send_message(chat_id=chat_id, text=f"""Welcome!\n\
I'll let you know when free games are available.\n\
You can also type /free to see all the free games I've found.\n\
If something is not clear, write the /help command.""",
                                    )

    elif lang == "ua":
        await bot.send_message(chat_id=chat_id, text=f"""Ласкаво просимо!\n\
Я вам повідомлю, коли з'являться безкоштовні ігри.
Також ви можете написати команду /free, щоб побачити всі безкоштовні ігри, які мені вдалося знайти.\n\
Якщо щось не зрозуміло пишіть команду /help.""",
                                    )

    elif lang == "ru":
        await bot.send_message(chat_id=chat_id, text=f'📜 Добро пожаловать <b>{last_name}</b>!\n📌 Сдесь вы можете заказать \
бота совсем дешево, по тому что мой создатель еще не опытен, не всех ботов сможет создать и \
делает их довольно долго (2-5 дней).\n📌 Если будут возникать ошибки обращайтесь к /help (Помощь). \
Больше информации есть в разделе "Дополнительное", "Информация".', parse_mode=ParseMode.HTML)



# ! Заказать бота
@router.callback_query(lambda call: call.data == "order")
async def order_bot(call: types.CallbackQuery):

    chat_id = call.message.chat.id
    msg_id = call.message.message_id
    lang = await get_chat_lang(chat_id)

    if lang == "ne":
        await bot.edit_message_text(chat_id=chat_id,
                              message_id=msg_id,
                              parse_mode=ParseMode.HTML,
                              reply_markup=order_bot_ikb(lang),
                              text="📌 If you want to order a bot, then there is a lot to discuss and you must tell us which bot you want. " +
                              "What would I write, click on the button under the message.")

    elif lang == "ua":
        await bot.edit_message_text(chat_id=chat_id,
                              message_id=msg_id,
                              parse_mode=ParseMode.HTML,
                              reply_markup=order_bot_ikb(lang),
                              text="📌 Якщо ви хочете замовити бота, то потрібно багато обговорити і ви повинні розповісти якогось бота хочете. " +
                              "Що б мені написати натисніть кнопку під повідомленням.")

    elif lang == "ru":
        await bot.edit_message_text(chat_id=chat_id,
                              message_id=msg_id,
                              parse_mode=ParseMode.HTML,
                              reply_markup=order_bot_ikb(lang),
                              text="📌 Если вы хотите заказать бота, то нужно многое обговорить и вы должны розказать какого бота хотите. " + 
                              "Что бы мне написать нажмите на кнопку под сообщением.")

        
    await sleep(24 * 60 * 60)
    await bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)



# ! command help
@router.callback_query(F.data == "help")
async def help(call: types.CallbackQuery):

    chat_id = call.message.chat.id
    lang = await get_chat_lang(chat_id)
    message_id = call.message.message_id

    if lang == "en":
        await bot.edit_message_text(chat_id=chat_id, message_id=message_id, 
                                text="""📚 List of commands:
/start - Bot welcome message
/help - If you need help
/free - View free games

If something is not clear to you, you can contact technical support (button under the message)""",
reply_markup=main_menu_back_ikb(lang))


    elif lang == "ua":
        await bot.edit_message_text(chat_id=chat_id, message_id=message_id, 
                                text="""📚 Список команд:
/start - Вітальне повідомлення бота
/help - Якщо потрібна допомога
/free - Перегляд безкоштовних ігор

Якщо вам щось не зрозуміло, то ви можете звернутися в техпідтримку (кнопка під повідомленням))""",
reply_markup=main_menu_back_ikb(lang))


    elif lang == "ru":
        await bot.edit_message_text(chat_id=chat_id, message_id=message_id, 
                                text="""📚 Список команд:
/start - Приветственое сообщение бота
/help  - Если нужна помощь
/free  - Просмотр бесплатных игор

Если вам что то не понятно то вы можете обратиться в техподдержку (кнопка под сообщением)""",
reply_markup=main_menu_back_ikb(lang))
        
    await sleep(24 * 60 * 60)
    await bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)



# ! Вопросы и ответы
@router.callback_query(F.data == "questions")
async def questions(call: types.CallbackQuery, state: FSMContext):

    await state.clear()

    chat_id = call.message.chat.id
    message_id = call.message.message_id
    lang = await get_chat_lang(chat_id)

    if lang == "en":
        await bot.edit_message_text(chat_id=chat_id,
                                message_id=message_id,
                                text="📌 <b>Here many of you can find answers to your questions.!</b>",
                                parse_mode=ParseMode.HTML,
                                reply_markup=woth_bot_ikb(lang))

    elif lang == "ua":
        await bot.edit_message_text(chat_id=chat_id,
                                message_id=message_id,
                                text="📌 <b>Тут багато хто з вас може знайти відповіді на свої запитання!</b>",
                                parse_mode=ParseMode.HTML,
                                reply_markup=woth_bot_ikb(lang))

    elif lang == "ru":
        await bot.edit_message_text(chat_id=chat_id,
                                message_id=message_id,
                                text="📌 <b>Здесь многие из вас могут найти ответы на свои вопросы!</b>",
                                parse_mode=ParseMode.HTML,
                                reply_markup=woth_bot_ikb(lang))

    await sleep(24 * 60 * 60)
    await bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)



@router.callback_query(F.data.startswith("???"))
async def questions_call(call: types.CallbackQuery):

    chat_id = call.message.chat.id
    message_id = call.message.message_id
    lang = await get_chat_lang(chat_id)

    question = call.data.split(" ")[1]

    if question == "kak_poishodit_zakaz":
        await bot.edit_message_text(chat_id=chat_id, 
                                    message_id=message_id, 
                                    text="❓ Как происходит заказ",
                                    reply_markup=main_or_questions_menu_ikb(lang))

    elif question == "skolko_stoit_hosting":
        await bot.edit_message_text(chat_id=chat_id, 
                                    message_id=message_id, 
                                    text="❓ Сколько стоит хостинг бота",
                                    reply_markup=main_or_questions_menu_ikb(lang))

    await sleep(24 * 60 * 60)
    await bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)



# ! Ссылки на мои проэкты
@router.callback_query(F.data == "projeсt")
async def project_bots(call: types.CallbackQuery):

    chat_id = call.message.chat.id
    msg_id = call.message.message_id
    lang = await get_chat_lang(chat_id)


    if lang == "en":
        await bot.edit_message_text(chat_id=chat_id, 
                                    message_id=msg_id, 
                                    parse_mode=ParseMode.HTML,
                                    reply_markup=free_games_ikb(lang),
                                    text="🤖 <b>My telegram bots:</b>\n\n" +
                                    
                                    "1️⃣ <b>Free Games</b>\n" +
                                    "Bot notifies you when new free games appear in " +
                                    "<b><u>Steam</u></b>, <b><u>GOG</u></b> and <b><u>Epic Games</u></b>. " +
                                    " By sending the title, picture and link (link to get the game) to the game.\n\n" +

                                    "2️⃣ <b>💬 Communication ...</b>\n" +
                                    "Feedback bot. When you write to the bot, it forwards the message to me," +
                                    "and then I already reply to the user's message in a PM with the bot and the bot sends it back to the person.")

    elif lang == "ua":
        await bot.edit_message_text(chat_id=chat_id, 
                                    message_id=msg_id, 
                                    parse_mode=ParseMode.HTML,
                                    reply_markup=free_games_ikb(lang),
                                    text="🤖 <b>Мої телеграм боти:</b>\n\n" +
                                    
                                    "1️⃣ <b>Free Games</b>\n" +
                                    "Бот вам повідомляє коли з'являються нові безкоштовні ігри в "
                                    "<b><u>Steam</u></b>, <b><u>GOG</u></b> та <b><u>Epic Games</u></b>. " +
                                    " Надсилаючи назву, картинку та посилання (посилання для отримання гри) на гру.\n\n" +

                                    "2️⃣ <b>💬 Спілкування ...</b>\n" +
                                    "Бот зворотного зв'язку. Коли ви пишіть боту, він пересилає це повідомлення мені," +
                                    "А після я вже в лс з ботом відповідаю на повідомлення користувача і бот відправляє його людині назад.")

    elif lang == "ru":
        await bot.edit_message_text(chat_id=chat_id, 
                                    message_id=msg_id, 
                                    parse_mode=ParseMode.HTML,
                                    reply_markup=free_games_ikb(lang),
                                    text="🤖 <b>Мои телеграм боты:</b>\n\n" + 
                                    
                                    "1️⃣ <b>Free Games</b>\n" +
                                    "Бот вам сообщяет когда появляються новые бесплатные игры в " +
                                    "<b><u>Steam</u></b>, <b><u>GOG</u></b> и <b><u>Epic Games</u></b>." +
                                    " Присылая название, картинку и ссылку (ссылка для получения игры) на игру.\n\n" +

                                    "2️⃣ <b>💬 Общение ...</b>\n" +
                                    "Бот обратной связи. Когда вы пишите боту, он пересылает это сообщение мне," +
                                    "а после я уже в лс с ботом отвечаю на сообщение пользователя и бот отправляет его человеку обратно.")
    
    await sleep(24 * 60 * 60)
    await bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)



# ! Настройка языка
@router.callback_query(F.data == "change_language")
async def change_language(call: types.CallbackQuery):

    chat_id = call.message.chat.id
    lang = await get_chat_lang(chat_id)

    if lang == "en":
        await bot.edit_message_text(chat_id=chat_id, 
                                    message_id=call.message.message_id, 
                                    text="🇺🇸 <b>Now you have Russian selected, you can choose another:</b>",
                                    parse_mode=ParseMode.HTML,
                                    reply_markup=change_language_ikb())

    elif lang == "ua":
        await bot.edit_message_text(chat_id=chat_id, 
                                    message_id=call.message.message_id, 
                                    text="🇺🇦 <b>Зараз у вас обраний український, можете вибрати інший:</b>",
                                    parse_mode=ParseMode.HTML,
                                    reply_markup=change_language_ikb())

    elif lang == "ru":
        await bot.edit_message_text(chat_id=chat_id, 
                                    message_id=call.message.message_id, 
                                    text="🇷🇺 <b>Сейчас у вас выбран русский, можете выбрать другой:</b>",
                                    parse_mode=ParseMode.HTML,
                                    reply_markup=change_language_ikb())
    
    await sleep(24 * 60 * 60)
    await bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)



@router.callback_query(F.data.startswith("update_"))
async def update_language(call: types.CallbackQuery):

    chat_id = call.message.chat.id
    lang = call.data.split("_")[1]

    await db.insert_settings(chat_id, lang)

    if lang == "en":
        await bot.edit_message_text(chat_id=chat_id, 
                                    message_id=call.message.message_id,
                                    text="<b>You have successfully changed the language to English!</b>",
                                    parse_mode=ParseMode.HTML,
                                    reply_markup=change_language_ikb())

    elif lang == "ua":
        await bot.edit_message_text(chat_id=chat_id, 
                                    message_id=call.message.message_id,
                                    text="<b>Ви успішно змінили мову на українську!</b>",
                                    parse_mode=ParseMode.HTML,
                                    reply_markup=change_language_ikb())

    elif lang == "ru":
        await bot.edit_message_text(chat_id=chat_id, 
                                    message_id=call.message.message_id,
                                    text="<b>Вы успешно сменили язык на русский!</b>",
                                    parse_mode=ParseMode.HTML,
                                    reply_markup=change_language_ikb())
    
    await sleep(24 * 60 * 60)
    await bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)



# ! В главное меню
@router.callback_query(F.data == "back")
async def main_menu_call(call: types.CallbackQuery, state: FSMContext):

    await state.clear()

    message_id = call.message.message_id
    chat_id = call.message.chat.id
    lang = await get_chat_lang(chat_id)

    if lang == "en":
        await bot.edit_message_text(chat_id=chat_id, 
                                    message_id=message_id,
                                    text="<b>Main menu!</b>",
                                    parse_mode=ParseMode.HTML,
                                    reply_markup=main_menu_ikb(lang))

    elif lang == "ua":
        await bot.edit_message_text(chat_id=chat_id, 
                                    message_id=message_id,
                                    text="<b>Головне меню!</b>",
                                    parse_mode=ParseMode.HTML,
                                    reply_markup=main_menu_ikb(lang))

    elif lang == "ru":
        await bot.edit_message_text(chat_id=chat_id, 
                                    message_id=message_id,
                                    text="<b>Главное меню!</b>",
                                    parse_mode=ParseMode.HTML,
                                    reply_markup=main_menu_ikb(lang))

    await sleep(24 * 60 * 60)
    await bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)



# ! Ответчаем на сообщение в техподдержке
@router.message()
async def technical_support_reply(msg: types.Message):
    
    if msg.reply_to_message:

        with open("config.json", "r") as f:
            config = load(f)
            id_support = config["technical_support_chat_id"]

        if str(msg.chat.id) == str(id_support):
            piple_id = msg.reply_to_message.text.split("\n")[0] # Получаем id человека

            await bot.send_message(chat_id=piple_id, text=f"{msg.text}\n\n<b></b>", parse_mode=ParseMode.HTML)
        
        else: 
            await bot.delete_message(chat_id=msg.chat.id, message_id=msg.message_id)

    else:
        await bot.delete_message(chat_id=msg.chat.id, message_id=msg.message_id)

