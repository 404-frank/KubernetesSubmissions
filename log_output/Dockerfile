FROM python:3.14-alpine

RUN apk update && apk add bash
COPY requirements.txt .
RUN pip install -r requirements.txt

WORKDIR /usr/src/app
RUN python -m venv /usr/src/app/.venv
ENV PATH="/usr/app/venv/bin:$PATH"

COPY . .


EXPOSE 5000

ENTRYPOINT ["nohup", "/usr/src/app/bash_start.sh"]
CMD ["sleep", "infinity"]
