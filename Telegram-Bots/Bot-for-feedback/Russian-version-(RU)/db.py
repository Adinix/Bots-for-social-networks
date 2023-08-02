import aiosqlite as sq

name_db = "users_id.db"

# Подключение к базе данных и создание таблицы 'chats' (если её нет)
async def connect_db_user():
    async with sq.connect(name_db) as db:
        await db.execute("CREATE TABLE IF NOT EXISTS chats(user_id INTEGER PRIMARY KEY, start_command INTEGER)")

        if db:
            print(f"{name_db} connection was successful!")

        await db.commit()


# Получение информации о чате по его идентификатору
async def get_chat_info(id):
    async with sq.connect(name_db) as conn:
        async with conn.cursor() as cur:
            cfg = await cur.execute("SELECT * FROM chats WHERE user_id == ?", (id,))
            cfg = await cfg.fetchall()
            return cfg


# Запись информации о пользователе (user_id) и его настройках (start_command) в базу данных
async def insert_settings(user_id, start_command):
    async with sq.connect(name_db) as conn:
        async with conn.cursor() as cur:
            cursor = await cur.execute("SELECT * FROM chats WHERE user_id = ?", (user_id,))
            examination = await cursor.fetchone()

            if examination:
                await cur.execute("UPDATE chats SET start_command = ? WHERE user_id = ?", (start_command, user_id))
            else:
                await cur.execute("INSERT INTO chats (user_id, start_command) VALUES (?, ?)", (user_id, start_command))

            await conn.commit()


# Обновление настройки 'start_command' для всех пользователей в базе данных
async def update_all_settings(start_command):
    async with sq.connect(name_db) as conn:
        async with conn.cursor() as cur:
            await cur.execute("UPDATE chats SET start_command = ?", (start_command,))
            await conn.commit()
