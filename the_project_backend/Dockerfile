FROM python:3.14-alpine

RUN apk update && apk add bash

WORKDIR /usr/src/app
RUN python -m venv /usr/src/app/venv
ENV PATH="/usr/src/app/venv/bin:$PATH"

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY listener.py ./
COPY globals.py ./
COPY todos.txt ./
COPY testing.py ./
COPY bash_start.sh ./

ENTRYPOINT ["nohup", "/usr/src/app/bash_start.sh"]
CMD ["sleep", "infinity"]
