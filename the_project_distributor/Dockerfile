##### first stage #####
FROM python:3.14-slim AS build-stage

RUN apt-get update

WORKDIR /usr/app
RUN python -m venv /usr/app/venv
ENV PATH="/usr/app/venv/bin:$PATH"

COPY requirements.txt .
RUN pip install -r requirements.txt

# ##### second stage #####
FROM python:3.14-slim
WORKDIR /usr/app
COPY --from=build-stage /usr/app/venv ./venv
COPY ./distributor.py .
COPY ./bash_start.sh .

RUN useradd -m appuser && \
    chown appuser .
USER appuser

ENV PATH="/usr/app/venv/bin:$PATH"
ENTRYPOINT ["nohup", "/usr/app/bash_start.sh"]
CMD ["sleep", "infinity"]

