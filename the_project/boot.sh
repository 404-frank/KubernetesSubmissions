#!/bin/sh

if [ -z ${LISTENING_PORT} ];
   then LISTENING_PORT=3000
fi

gunicorn app:app \
	--workers 1 \
	--threads 2 \
	--bind 0.0.0.0:${LISTENING_PORT} \
	--capture-output \
	--access-logfile '-' \
	--error-logfile '-'
