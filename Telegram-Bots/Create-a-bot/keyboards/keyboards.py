from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


# ! /start
async def start_kb(lang):
    
    if lang == "en":
        start = KeyboardButton(text='🔘 Menu 🔘')
        start_kb = ReplyKeyboardMarkup(keyboard=start, resize_keyboard=True, input_field_placeholder='"📖 Помощь" Если что то не понятно')

    elif lang == "ua":
        start = KeyboardButton(text='🔘 Меню 🔘')
        start_kb = ReplyKeyboardMarkup(keyboard=start, resize_keyboard=True, input_field_placeholder='"📖 Помощь" Если что то не понятно')

    elif lang == "ru":
        start = KeyboardButton(text='🔘 Меню 🔘')
        start_kb = ReplyKeyboardMarkup(keyboard=start, resize_keyboard=True, input_field_placeholder='"📖 Помощь" Если что то не понятно')

    return start_kb



# ! Выход из машиного состояния
async def FSM_exit_kb(lang):

    if lang == "en":
        FSM_exit_kb = ReplyKeyboardMarkup(resize_keyboard=True, input_field_placeholder='"📖 Помощь" Если что то не понятно')
        cancel = KeyboardButton("❌ Cancel ❌")

    elif lang == "ua":
        FSM_exit_kb = ReplyKeyboardMarkup(resize_keyboard=True, input_field_placeholder='"📖 Помощь" Если что то не понятно')
        cancel = KeyboardButton("❌ Відміна ❌")

    elif lang == "ru":
        FSM_exit_kb = ReplyKeyboardMarkup(resize_keyboard=True, input_field_placeholder='"❌ Отмена ❌" Что-бы отменить действие')
        cancel = KeyboardButton("❌ Отмена ❌")

    return FSM_exit_kb.add(cancel)
