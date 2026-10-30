import asyncio
import json
import requests
import os

from nats.aio.client import Client as NATS

NATS_URL = os.environ.get('NATS_URL', 'nats://my-nats:4222')
NATS_TODO_QUEUE = os.environ.get('NATS_TODO_QUEUE', 'distribute')
EXTERNAL_SUBMIT_SERVICE = os.environ.get('EXTERNAL_SUBMIT_SERVICE',
 'https://jsonplaceholder.typicode.com/todos')

print("starting Distributor service...")

async def main() -> None:
    nc = NATS()
    await nc.connect(servers=[NATS_URL])
    async def saver_data_cb(msg):
        payload = json.loads(msg.data.decode())
        print(f"Received todo from backend, payload [{payload}]")
        send_to_jsonPlaceHolder(addJson(payload))
    await nc.subscribe(NATS_TODO_QUEUE, cb=saver_data_cb)
    print(f"Distributor is listening on: [{NATS_URL}]")
    await asyncio.Future()

def send_to_jsonPlaceHolder(payload: str):
    headers = {'Content-type': 'application/json'}
    try:
        print(f'Submitting todo to jsonplaceholder site')
        response = requests.post(EXTERNAL_SUBMIT_SERVICE, json=payload, headers=headers)
        response.raise_for_status()  # Raise HTTPError for bad responses (4xx or 5xx)
        response_data = response.json()
        print(f'Response Data: {response_data}')
        print(f'Status Code: {response.status_code}')
    except requests.exceptions.HTTPError as errh:
        print(f'HTTP Error: {errh}')
    except requests.exceptions.ConnectionError as errc:
        print(f'Connection Error: {errc}')
    except requests.exceptions.Timeout as errt:
        print(f'Timeout Error: {errt}')
    except requests.exceptions.RequestException as err:
        print(f'Something went wrong: {err}')

def addJson(payload: json) -> json:
    payload["original_id"] = payload["id"]
    return payload

if __name__ == "__main__":
    asyncio.run(main())