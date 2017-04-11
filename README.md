# Skype to Telegram Gateway

Establishes 2 way text messaging between telegram chat and skype contacts

## Getting Started

Bot communicates only with added contacts, so before start, add all necessary people manually from https://web.skype.com

To run locally:

```
pip install -r requirements.txt
export "TELEGRAM_TOKEN=<token>"
export "TELEGRAM_CHAT_ID=<chat id:-212121212>"
export "SKYPE_LOGIN=<login>"
export  "SKYPE_PASSWORD=<password>"
export  "SKYPE_SUBSCRIBERS=<comma separated skype logins>"

python3 ./main.py
```

To run in docker:
```
docker build -t stt_gw .
docker run --name=stt_gw \
  -e "TELEGRAM_TOKEN=<token>"\
  -e "TELEGRAM_CHAT_ID=<chat id:-212121212>"\
  -e "SKYPE_LOGIN=<login>"\
  -e "SKYPE_PASSWORD=<password>"\
  -e "SKYPE_SUBSCRIBERS=<comma separated skype logins>"\
   stt_gw
```
