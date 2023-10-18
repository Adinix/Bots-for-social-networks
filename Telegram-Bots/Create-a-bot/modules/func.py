from data_base import db


# ! Получаю язык который настроен на чат
async def get_chat_lang(chat_id):
    cfg = await db.get_chat_info(chat_id)

    try:
        lang = cfg[0][1]

    except IndexError:
        return None

    return lang

