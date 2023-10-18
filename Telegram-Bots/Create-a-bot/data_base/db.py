import sqlite3
import aiosqlite as sq


name_db = "chat_list.db"

# ! Создаем базу данных в которой будет скписок чатов и их настройки
async def connect_db_user():
    async with sq.connect(name_db) as db:

        await db.execute("CREATE TABLE IF NOT EXISTS chats(chat_id INTEGER PRIMARY KEY, language TEXT, first_name TEXT, last_name TEXT, user_name TEXT, language_code TEXT, title TEXT, type TEXT, all_members_are_administrators INTEGER)")

        if db:
            print(f"{name_db} connection was successful")

        await db.commit()



# ! Получаем всю информацию о чате
async def get_chat_info(id):
    async with sq.connect(name_db) as conn:
        async with conn.cursor() as cur:

            cfg = await cur.execute("SELECT * FROM chats WHERE chat_id == ?", (id,))
            cfg = await cfg.fetchall()

            return cfg



# ! Записываем информацию о пользователе
async def insert_settings(chat_id, language=None, first_name=None, last_name=None, user_name=None, language_code=None, title=None, type=None, all_members_are_administrators=None):
    async with sq.connect(name_db) as conn:
        async with conn.cursor() as cur:

            cursor = await cur.execute("SELECT * FROM chats WHERE chat_id = ?", (chat_id,))
            examination = await cursor.fetchone()

            if examination:

                if language == None:
                    language = examination[1]

                if first_name == None:
                    first_name = examination[2]

                if last_name == None:
                    last_name = examination[3]

                if user_name == None:
                    user_name = examination[4]

                if language_code == None:
                    language_code = examination[5]

                if title == None:
                    title = examination[6]

                if type == None:
                    type = examination[7]

                if all_members_are_administrators == None:
                    all_members_are_administrators = examination[8]

                await cur.execute("UPDATE chats SET language = ?, first_name = ?, last_name = ?, user_name = ?, language_code = ?, title = ?, type = ?, all_members_are_administrators = ? WHERE chat_id = ?", 
                                    (language, first_name, last_name, user_name, language_code, title, type, all_members_are_administrators, chat_id))

            else:
                await cur.execute("INSERT INTO chats (chat_id, language, first_name, last_name, user_name, language_code, title, type, all_members_are_administrators) VALUES (?,?,?,?,?,?,?,?,?)", 
                                                    ( chat_id, language, first_name, last_name, user_name, language_code, title, type, all_members_are_administrators))

            await conn.commit()



# ! Получаем id всех чатов
async def get_chats_id():
    async with sq.connect(name_db) as conn:
        async with conn.cursor() as cur:

            cursor = await cur.execute("SELECT chat_id FROM chats")
            cursor = await cursor.fetchall()

            return cursor