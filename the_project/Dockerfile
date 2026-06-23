##### first stage #####
FROM python:3.13-slim AS build-stage

RUN apt-get update
RUN apt-get install -y --no-install-recommends \
	build-essential gcc

WORKDIR /usr/app
RUN python -m venv /usr/app/venv
ENV PATH="/usr/app/venv/bin:$PATH"

COPY requirements.txt .
RUN pip install -r requirements.txt

##### second stage #####
FROM python:3.13-slim
WORKDIR /usr/app
COPY --from=build-stage /usr/app/venv ./venv
COPY . .

ENV LISTENING_PORT=3000
RUN useradd -m appuser && \
    chown appuser .
USER appuser

ENV PATH="/usr/app/venv/bin:$PATH"
ENTRYPOINT ["./boot.sh"]
