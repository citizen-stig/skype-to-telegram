import os
import logging
from skype_agent import SkypeAgent
from telegram_agent import TelegramAgent
from gateway import GateWay


def main():
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                        level=logging.INFO)
    telegram_token = os.environ['TELEGRAM_TOKEN']
    telegram_chat_id = int(os.environ['TELEGRAM_CHAT_ID'])
    skype_login = os.environ['SKYPE_LOGIN']
    skype_password = os.environ['SKYPE_PASSWORD']
    skype_subscribers = os.environ['SKYPE_SUBSCRIBERS'].split(',')

    gw = GateWay()

    skype_agent = SkypeAgent(user=skype_login,
                             pwd=skype_password,
                             message_handler=gw.send_message_to_telegram,
                             subscribers=skype_subscribers)
    telegram_agent = TelegramAgent(token=telegram_token,
                                   chat_id=telegram_chat_id,
                                   message_handler=gw.send_message_to_skype)

    gw.set_skype_agent(skype_agent)
    gw.set_telegram_agent(telegram_agent)

    gw.run()


if __name__ == '__main__':
    main()
