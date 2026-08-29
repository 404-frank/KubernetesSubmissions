#!/bin/sh
# Docker entrypoint script with error handling
set -e

# Log messages with timestamps for easier debugging
log() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $*"
}

# Log errors to stderr
error() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] ERROR: $*" >&2
}

log "Starting entrypoint script"

log "starting listener.py"
python -u listener.py &
log "started scripts in background"

sleep 20

log "Initialization complete, starting application"
exec "$@"