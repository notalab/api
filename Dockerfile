FROM python:3.6-alpine

RUN adduser -D nota
RUN apk update
RUN apk add postgresql-dev gcc python3-dev musl-dev libffi-dev

WORKDIR /home/nota

COPY requirements.txt requirements.txt
RUN python -m venv venv
RUN venv/bin/pip install -r requirements.txt
RUN venv/bin/pip install gunicorn

COPY ./src /app
COPY ./migrations /migrations
COPY .env.example .env
COPY entrypoint.sh .

ENV FLASK_APP server.py

RUN chown -R nota:nota ./
USER nota

RUN chmod +x entrypoint.sh

EXPOSE 5000
ENTRYPOINT [ "./entrypoint.sh" ]
