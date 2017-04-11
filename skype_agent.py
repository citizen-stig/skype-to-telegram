import logging
from typing import Callable
from skpy import SkypeEventLoop
from skpy import SkypeNewMessageEvent


class SkypeAgent(SkypeEventLoop):
    def __init__(self, message_handler: Callable, subscribers: list = None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.message_handler = message_handler
        self.subscribers = subscribers if subscribers else []
        self.logger = logging.getLogger('skype_agent')
        self.logger.info('Skype Agent initialization completed: subscribers=%s, message_hander=%s',
                         self.subscribers, self.message_handler)

    def _process_input_message(self, event: SkypeNewMessageEvent):
        if event.msg.userId != self.userId:
            new_message = '{0}: {1}'.format(event.msg.user.name, event.msg.content)
            self.logger.debug('Processing input message: "%s"', new_message)
            self.message_handler(new_message)

    def send_message_to_subscribers(self, message):
        self.logger.debug('Sending message "%s" to subscribers', message)
        for nick in self.subscribers:
            contact = self.contacts[nick]
            if contact:
                contact.chat.sendMsg(message)
            else:
                self.logger.warning('Nick %s is not in contacts!', nick)

    def onEvent(self, event):
        if isinstance(event, SkypeNewMessageEvent):
            self._process_input_message(event)
