#!/bin/sh

gunicorn app:app \
	--workers 1 \
	--threads 2 \
	--bind 0.0.0.0:${LISTENING_PORT} \
	--capture-output \
	--access-logfile '-' \
	--error-logfile '-'
