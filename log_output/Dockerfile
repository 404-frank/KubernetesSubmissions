FROM python:3.14-alpine

RUN apk update && apk add bash

WORKDIR /usr/src/app
COPY listener.py ./
COPY start.py ./
COPY globals.py ./
COPY bash_start.sh ./

EXPOSE 5000

# CMD [ "python", "-u", "./listener.py" ]
# CMD [ "python", "-u", "./start.py" ]
ENTRYPOINT ["nohup", "/usr/src/app/bash_start.sh"]
CMD ["sleep", "infinity"]
