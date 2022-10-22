FROM python:3.9-slim-buster
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY cronsql.py .
COPY config.yaml .
CMD ["python", "./cronsql.py"]