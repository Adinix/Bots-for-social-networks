from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder


# ! Главное меню
def main_menu_ikb(lang):

    if lang == "en":
        order = InlineKeyboardButton    (text="👑 Order a bot", callback_data="order")
        questions = InlineKeyboardButton(text="❓ Questions and answers", callback_data='questions')
        projecs = InlineKeyboardButton  (text="💾 View projects", callback_data='projeсt')
        settings = InlineKeyboardButton (text="⚙️ Change language", callback_data="change_language")
        help = InlineKeyboardButton     (text="📖 Help", callback_data="help")

    elif lang == "ua":
        order = InlineKeyboardButton    (text="👑 Замовити бота", callback_data="order")
        questions = InlineKeyboardButton(text="❓ Питання та відповіді", callback_data='questions')
        projecs = InlineKeyboardButton  (text="💾 Подивитися на проекти", callback_data='projeсt')
        settings = InlineKeyboardButton (text="⚙️ Змінити мову", callback_data="change_language")
        help = InlineKeyboardButton     (text="📖 Допомога", callback_data="help")

    elif lang == "ru":
        order = InlineKeyboardButton    (text="👑 Заказать бота", callback_data="order")
        questions = InlineKeyboardButton(text="❓ Вопросы и ответы", callback_data='questions')
        projecs = InlineKeyboardButton  (text="💾 Посмотреть на проекты", callback_data='projeсt')
        settings = InlineKeyboardButton (text="⚙️ Сменить язык", callback_data="change_language")
        help = InlineKeyboardButton     (text="📖 Помощь", callback_data="help")

    menu = InlineKeyboardBuilder()
    menu.row(order).row(settings, help).row(projecs).row(questions)

    return menu.as_markup()



# ! Заказать бота
def order_bot_ikb(lang):

    link_user = InlineKeyboardButton(text="@regression_FF", url="https://t.me/regression_FF")

    if lang == "en":
        back = InlineKeyboardButton(text="👈 Back", callback_data="back")

    elif lang == "ua":
        back = InlineKeyboardButton(text="👈 Назад", callback_data="back")

    elif lang == "ru":
        back = InlineKeyboardButton(text="👈 Назад", callback_data="back")

    ikb = InlineKeyboardBuilder().add(link_user).add(back)


    return ikb.as_markup()


# ! Первый вызов start
def lang_ikb():

    en = InlineKeyboardButton(text="🇺🇸", callback_data=f"choice_lang_en")
    ua = InlineKeyboardButton(text="🇺🇦", callback_data=f"choice_lang_ua")
    ru = InlineKeyboardButton(text="🇷🇺", callback_data=f"choice_lang_ru")

    language_ikb = InlineKeyboardBuilder().row(en, ua, ru)

    return language_ikb.as_markup()



# ! Help
def main_menu_back_ikb(lang):

    if lang == "en":
        question = InlineKeyboardButton(text='❓ Ask a Question', callback_data='send_message_technical_support_h')
        back = InlineKeyboardButton(text="👈 Back", callback_data="back")

    elif lang == "ua":
        question = InlineKeyboardButton(text='❓ Задати питання', callback_data='send_message_technical_support_h')
        back = InlineKeyboardButton(text="👈 Назад", callback_data="back")

    elif lang == "ru":
        question = InlineKeyboardButton(text='❓ Задать вопрос', callback_data='send_message_technical_support_h')
        back = InlineKeyboardButton(text="👈 Назад", callback_data="back")


    help = InlineKeyboardBuilder().add(question).add(back)

    return help.as_markup()



# ! Настройки 
def change_language_ikb():

    lang_en = InlineKeyboardButton(text="🇺🇸", callback_data="update_en")
    lang_ua = InlineKeyboardButton(text="🇺🇦", callback_data="update_ua")
    lang_ru = InlineKeyboardButton(text="🇷🇺", callback_data="update_ru")
    back = InlineKeyboardButton(text="👈 Back", callback_data="back")

    settings = InlineKeyboardBuilder().add(lang_en).row(lang_ua, lang_ru).row(back)

    return settings.as_markup()


# ! Вопросы
def woth_bot_ikb(lang):

    if lang == "en":
        ikb = InlineKeyboardBuilder().row(\
            InlineKeyboardButton(text='❓ How is the order', callback_data='??? kak_poishodit_zakaz')).row(\
            InlineKeyboardButton(text='❓ How much does bot hosting cost', callback_data='??? skolko_stoit_hosting')).row(\
            InlineKeyboardButton(text='❓ Ask your question', callback_data='send_message_technical_support_q')).row(\
            InlineKeyboardButton(text="👈 Back", callback_data="back"))

    elif lang == "ua":
        ikb = InlineKeyboardBuilder().row(\
            InlineKeyboardButton(text='❓ Як відбувається замовлення', callback_data='??? kak_poishodit_zakaz')).row(\
            InlineKeyboardButton(text='❓ Скільки коштує хостинг бота', callback_data='??? skolko_stoit_hosting')).row(\
            InlineKeyboardButton(text='❓ Поставити своє запитання', callback_data='send_message_technical_support_q')).row(\
            InlineKeyboardButton(text="👈 Назад", callback_data="back"))

    elif lang == "ru":
        ikb = InlineKeyboardBuilder().row(\
            InlineKeyboardButton(text='❓ Как происходит заказ', callback_data='??? kak_poishodit_zakaz')).row(\
            InlineKeyboardButton(text='❓ Сколько стоит хостинг бота', callback_data='??? skolko_stoit_hosting')).row(\
            InlineKeyboardButton(text='❓ Задать свой вопрос', callback_data='send_message_technical_support_q')).row(\
            InlineKeyboardButton(text="👈 Назад", callback_data="back"))

    return ikb.as_markup()



def main_or_questions_menu_ikb(lang):

    if lang == "en":
        back_menu = InlineKeyboardButton(text="👈 Back to menu", callback_data="back")
        back_quest = InlineKeyboardButton(text="👈 Back to questions", callback_data="questions")

    elif lang == "ua":
        back_menu = InlineKeyboardButton(text="👈 Назад до меню", callback_data="back")
        back_quest = InlineKeyboardButton(text="👈 Назад до питань", callback_data="questions")

    elif lang == "ru":
        back_menu = InlineKeyboardButton(text="👈 Назад к меню", callback_data="back")
        back_quest = InlineKeyboardButton(text="👈 Назад к вопросам", callback_data="questions")


    ikb = InlineKeyboardBuilder().row(back_quest).row(back_menu)

    return ikb.as_markup()


def main_or_help_menu_ikb(lang):

    if lang == "en":
        back_menu = InlineKeyboardButton(text="👈 Back to menu", callback_data="back")
        back_help = InlineKeyboardButton(text="👈 Back to help", callback_data="help")

    elif lang == "ua":
        back_menu = InlineKeyboardButton(text="👈 Назад до меню", callback_data="back")
        back_help = InlineKeyboardButton(text="👈 Назад до допомоги", callback_data="help")

    elif lang == "ru":
        back_menu = InlineKeyboardButton(text="👈 Назад к меню", callback_data="back")
        back_help = InlineKeyboardButton(text="👈 Назад к помощи", callback_data="help")


    ikb = InlineKeyboardBuilder().row(back_help).row(back_menu)

    return ikb.as_markup()



# ! Мои проэкты
# ? Free Games bot
def free_games_ikb(lang):

    bot_1 = InlineKeyboardButton(text="1️⃣ Free Games", url="https://t.me/Free_Games_FF_Bot")
    bot_2 = InlineKeyboardButton(text="2️⃣ 💬 Общение ...", url="https://t.me/AI_for_communication_bot")

    if lang == "en":
        back = InlineKeyboardButton(text="👈 Back", callback_data="back")

    elif lang == "ua":
        back = InlineKeyboardButton(text="👈 Назад", callback_data="back")

    elif lang == "ru":
        back = InlineKeyboardButton(text="👈 Назад", callback_data="back")


    ikb = InlineKeyboardBuilder().row(bot_1).row(bot_2).row(back)

    return ikb.as_markup()