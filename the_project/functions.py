import os
from datetime import datetime
import requests

LOCAL_IMAGE_STORE_URL = os.environ.get('LOCAL_IMAGE_STORE_URL', './static/temp_image.png')
LOCAL_IMAGE_WEBSERVER_URL = os.environ.get('LOCAL_IMAGE_WEBSERVER_URL', '/static/sharedfiles/temp_image.png')
REMOTE_IMAGE_RETRIEVAL_URL = os.environ.get('REMOTE_IMAGE_RETRIEVAL_URL', 'https://picsum.photos/1200')
BACKEND_SERVER_URL = os.environ.get('BACKEND_SERVER_URL', 'http://localhost:3001/todos')

def get_image_url():
    if image_too_old(LOCAL_IMAGE_STORE_URL):
        # get new one
        retrieve_new_image()
    return LOCAL_IMAGE_WEBSERVER_URL


def image_too_old(imageFileName: str) -> bool:
    if os.path.isfile(imageFileName):
        mtime = datetime.fromtimestamp(os.path.getmtime(imageFileName))
        time_diff_seconds = int((datetime.now() - mtime).total_seconds())
        return time_diff_seconds > 600
    return True

def retrieve_new_image():
    response = requests.get(REMOTE_IMAGE_RETRIEVAL_URL, headers={"User-Agent": "Mozilla/5.0"})
    image_data = response.content
    with open(LOCAL_IMAGE_STORE_URL, 'wb') as handler:
        handler.write(image_data)

def get_todos() -> list:
    response = requests.get(BACKEND_SERVER_URL, headers={"User-Agent": "Mozilla/5.0"})
    decoded_response = response.content.decode("UTF-8")
    todo_list = eval(decoded_response)
    return todo_list
    # strip empty lines
    # return [item for item in todo_list if item.strip()]