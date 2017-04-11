import logging
from threading import Thread
from skype_agent import SkypeAgent
from telegram_agent import TelegramAgent


class GateWay(object):
    def __init__(self):
        self.skype_agent = None  # type: SkypeAgent
        self.telegram_agent = None  # type: TelegramAgent
        self.logger = logging.getLogger('gateway')

    def set_skype_agent(self, skype_agent: SkypeAgent):
        self.skype_agent = skype_agent

    def set_telegram_agent(self, telegram_agent: TelegramAgent):
        self.telegram_agent = telegram_agent

    def send_message_to_skype(self, message):
        if self.skype_agent:
            self.logger.debug('Sending message %s to skype subscribers', message)
            self.skype_agent.send_message_to_subscribers(message)
        else:
            self.logger.warning('Skype Agent has not been set yet')

    def send_message_to_telegram(self, message):
        if self.telegram_agent:
            self.logger.debug('Sending message %s to telegram', message)
            self.telegram_agent.send_message_to_group(message)
        else:
            self.logger.warning('Telegram Agent has not been set yet')

    def run(self):
        self.logger.info('Starting gateway...')
        skype_agent_thread = Thread(target=self.skype_agent.loop)
        telegram_agent_thread = Thread(target=self.telegram_agent.run)

        skype_agent_thread.start()
        telegram_agent_thread.start()
        self.logger.info('Threads have been started')

        skype_agent_thread.join()
        telegram_agent_thread.join()
