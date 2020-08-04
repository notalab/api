FROM python:3.6-alpine

RUN adduser -D nota
RUN apk update
RUN apk add postgresql-dev gcc python3-dev musl-dev libffi-dev

WORKDIR /home/nota

COPY requirements-dev.txt requirements.txt ./
RUN pip install -r requirements-dev.txt --upgrade --no-warn-script-location
RUN pip install gunicorn

COPY . ./
COPY .env.example ./.env
COPY entrypoint.sh .

ENV FLASK_APP server.py

RUN chown -R nota:nota ./
USER nota

RUN chmod +x entrypoint.sh

EXPOSE 5000 8000
ENTRYPOINT [ "sh", "./entrypoint.sh" ]
