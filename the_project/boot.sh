#!/bin/sh

if [ -z ${SERVER_LISTENING_PORT} ];
   then SERVER_LISTENING_PORT=3000
fi
port_string=${SERVER_LISTENING_PORT}
port_int=$((port_string))
echo "starting gunicorn service on: $port_int"

gunicorn app:app \
	--workers 1 \
	--threads 2 \
	--bind ${SERVER_LISTENING_URL}:$port_int \
	--capture-output \
	--access-logfile '-' \
	--error-logfile '-'
