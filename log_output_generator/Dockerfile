FROM python:3.14-alpine

RUN apk update && apk add bash

WORKDIR /usr/src/app
COPY generator.py ./
COPY globals.py ./
COPY vars.txt ./files/vars.txt
COPY bash_start.sh ./

EXPOSE 5000

ENTRYPOINT ["nohup", "/usr/src/app/bash_start.sh"]
CMD ["sleep", "infinity"]
