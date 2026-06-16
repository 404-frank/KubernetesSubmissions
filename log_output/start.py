import uuid
from time import sleep
import datetime

while True:
    _uuid = uuid.uuid4()
    time_stamp = datetime.datetime.now()
    base = time_stamp.strftime('%Y-%m-%dT%H:%M:%S')
    millis = int(time_stamp.strftime('%f')) / 1000
    print(f"{base}.{millis:03.0f}Z: {_uuid}")
    sleep(5)
