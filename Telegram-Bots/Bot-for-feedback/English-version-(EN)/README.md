# About the Bot

This bot is a tool for communication and interaction with users through Telegram. It is developed using Python and utilizes the Aiogram library to interact with the Telegram Bot API. The bot is capable of responding to various commands and processing different types of messages, such as text messages, photos, audio, video, documents, and stickers. Additionally, it supports responding to messages with specified media types and handles replies to its own sent messages.

## Description

This bot is developed using [Python](https://www.python.org/) and [Aiogram](https://github.com/aiogram/aiogram) for interacting with the [Telegram Bot API](https://core.telegram.org/bots/api).

# Installation

1. Clone the repository:

```bash
git clone https://github.com/Adinix/Social-media-bots.git
cd Telegram-Bots/AI_for_Communication_bot/Russian version (RU)
```

2. Install the dependencies

```bash
pip install -r requirements.txt
```

### Bot Launch

```bash
python main.py
```

# Functionality

### Commands:
1. /start - Begin communication with the bot.
2. /chat_info - Get information about the user and the chat.

Additional Handlers
Handler for Files and Regular Messages

The handle_files_and_text handler is responsible for processing files (documents, audio, photos, video, voice messages, stickers) and regular text messages received by the bot. It sends user information and the content of the message to the chat id_com.
Handler for Replies to Files and Regular Messages

The handle_reply_files_and_text handler is responsible for processing replies to files (documents, audio, photos, video, voice messages, stickers) and regular text messages. It sends user information and the content of the replied message to the chat id_com.

## More about the functionality

1. Command responses: The bot processes the /start command, which allows users to initiate communication with it. Upon the first run, the bot greets the user and adds them to the database. Upon subsequent runs, if the user already exists in the database, the bot sends information about the user to the specified chat id_com.

2. Sending information: Upon receiving the /chat_info command, the bot sends information about the current chat from which the command was sent. This includes user information, such as their name, surname, username, and ID.

3. Handling various message types: The bot supports the processing of various message types, including text messages, photos, audio, video, documents, and stickers. Upon receiving a message of a specified type, the bot responds to it and sends user information to the chat id_com.

4. Handling reply messages: The bot handles replies to its sent messages with various media files. When a user responds to a bot's message containing media, the bot forwards it to the chat id_com and adds information about the user who sent the reply.

5. Protection against groups and channels: The bot only responds to messages sent from a personal chat (not from a group or channel). If the /start or /chat_info command is sent from a group or channel, the bot responds with a notification about it.

6. Notification on blocking: If a user blocks the bot and attempts to reply to its message, the bot sends a notification to the chat id_com that this user has blocked the bot.

7. Interface for adding new handlers: The bot provides an easy way to add new handlers for different message types, expanding the bot's functionality to handle other types of media and commands.
