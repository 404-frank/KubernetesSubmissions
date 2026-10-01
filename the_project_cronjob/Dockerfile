FROM python:3.14-alpine

RUN apk update && apk add bash

WORKDIR /usr/src/app
RUN python -m venv /usr/src/app/venv
ENV PATH="/usr/src/app/venv/bin:$PATH"

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY insert_todo.py ./

ENTRYPOINT ["python", "/usr/src/app/insert_todo.py"]

