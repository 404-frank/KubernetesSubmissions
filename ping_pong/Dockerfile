FROM python:3.14-alpine

WORKDIR /usr/src/app

RUN apk update && \
    apk add libpq-dev && \
    apk add bash
COPY requirements.txt .
RUN pip install --upgrade pip && \
    pip install --upgrade setuptools wheel && \
    pip install --no-cache-dir --upgrade -r requirements.txt

COPY . .
RUN rm requirements.txt

EXPOSE 5100

ENTRYPOINT ["nohup", "/usr/src/app/bash_start.sh"]
CMD ["sleep", "infinity"]
