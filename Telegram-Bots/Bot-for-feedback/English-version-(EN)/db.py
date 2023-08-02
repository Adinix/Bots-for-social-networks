import aiosqlite as sq

name_db = "users_id.db"

# Connect to the database and create the 'chats' table (if it doesn't exist)
async def connect_db_user():
    async with sq.connect(name_db) as db:
        await db.execute("CREATE TABLE IF NOT EXISTS chats(user_id INTEGER PRIMARY KEY, start_command INTEGER)")

        if db:
            print(f"{name_db} connection was successful!")

        await db.commit()


# Get chat information by its identifier
async def get_chat_info(id):
    async with sq.connect(name_db) as conn:
        async with conn.cursor() as cur:
            cfg = await cur.execute("SELECT * FROM chats WHERE user_id == ?", (id,))
            cfg = await cfg.fetchall()
            return cfg


# Write user information (user_id) and their settings (start_command) to the database
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


# Update the 'start_command' setting for all users in the database
async def update_all_settings(start_command):
    async with sq.connect(name_db) as conn:
        async with conn.cursor() as cur:
            await cur.execute("UPDATE chats SET start_command = ?", (start_command,))
            await conn.commit()
