import uuid
from time import sleep
import datetime
import os
import globals

while True:
    _uuid = uuid.uuid4()
    time_stamp = datetime.datetime.now()
    base = time_stamp.strftime('%Y-%m-%dT%H:%M:%S')
    millis = int(time_stamp.strftime('%f')) / 1000
    _random_string = f"{base}.{millis:03.0f}Z: {_uuid}"
    print(_random_string)
    globals.set_random_string(_random_string)
    sleep(5)
