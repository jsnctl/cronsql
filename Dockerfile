FROM python:3.9-slim-buster
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
RUN apt-get update && apt-get install -y cron
COPY . .
COPY config.yaml /root/config.yaml
RUN python parse.py
RUN /usr/bin/crontab crontab
CMD ["cron", "-f"]