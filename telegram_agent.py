from typing import Callable
import telegram
from telegram.ext import Updater, MessageHandler, Filters


class TelegramAgent(object):

    def __init__(self, token: str, chat_id: int, message_handler: Callable):
        self.token = token
        self.chat_id = chat_id
        self.message_handler = message_handler
        self.updater = Updater(token=token)
        self.bot = telegram.Bot(token=token)

    def send_message_to_group(self, message: str):
        self.bot.sendMessage(chat_id=str(self.chat_id), text=message)

    def get_group_chat_handler(self):
        def callback(bot, update):
            message = update['message']
            if message.chat.id == self.chat_id:
                msg = '{0}: {1}'.format(message.from_user.username, message.text)
                self.message_handler(msg)
        handler = MessageHandler(Filters.text, callback)
        return handler

    def run(self):
        self.updater.dispatcher.add_handler(self.get_group_chat_handler())
        self.updater.start_polling()
