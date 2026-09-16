FROM python:3.14-alpine

RUN apk update && apk add bash

WORKDIR /usr/src/app
COPY listener.py ./
COPY globals.py ./
COPY todos.txt ./
COPY bash_start.sh ./

EXPOSE 3001

ENTRYPOINT ["nohup", "/usr/src/app/bash_start.sh"]
CMD ["sleep", "infinity"]
