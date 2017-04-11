FROM python:3.5

ADD . /opt/stt_gw

RUN pip install -r /opt/stt_gw/requirements.txt

CMD [ "python", "/opt/stt_gw/main.py" ]
