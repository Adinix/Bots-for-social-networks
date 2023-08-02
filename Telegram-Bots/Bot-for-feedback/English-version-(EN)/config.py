from os import getenv

# Bot token
TOKEN = getenv("TOKEN")

# How often the bot will respond to the /start command; i.e., the minimum time that must pass before the bot responds again to the command
timer = 604800  # 7 days

# Chat ID where the bot will send everything it is written and you will respond to messages (it must be a group ID)
chat_bot_communication = -999193429
