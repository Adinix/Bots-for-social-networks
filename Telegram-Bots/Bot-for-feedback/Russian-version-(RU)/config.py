from os import getenv

# Токен бота
TOKEN = getenv("TOKEN")

# Как часто бот будет отвечать на команду /start, то есть минимум должно пройти это время перед тем как бот снова ответит на команду
timer = 604800 # 7 дней

# ID чата в который бот будет скидывать все что ему написали и вы тут будете отвечать на сообщения (обезательно нужно ID группы)
chat_bot_communication = -999193429 
