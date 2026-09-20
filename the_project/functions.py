import os
from datetime import datetime
import requests
LOCAL_IMAGE_STORE_URL = os.environ['LOCAL_IMAGE_STORE_URL']
LOCAL_IMAGE_WEBSERVER_URL = os.environ['LOCAL_IMAGE_WEBSERVER_URL']
REMOTE_IMAGE_RETRIEVAL_URL = os.environ['REMOTE_IMAGE_RETRIEVAL_URL']

def get_image_url():
    if image_too_old(os.environ['LOCAL_IMAGE_STORE_URL']):
        # get new one
        retrieve_new_image()
    return LOCAL_IMAGE_WEBSERVER_URL


def image_too_old(imageFileName: str) -> bool:
    if os.path.isfile(imageFileName):
        mtime = datetime.fromtimestamp(os.path.getmtime(imageFileName))
        time_diff_seconds = int((datetime.now() - mtime).total_seconds())
        # print(time_diff_seconds)
        return time_diff_seconds > 600
    return True

def retrieve_new_image():
    response = requests.get(REMOTE_IMAGE_RETRIEVAL_URL, headers={"User-Agent": "Mozilla/5.0"})
    image_data = response.content
    with open(os.environ['LOCAL_IMAGE_STORE_URL'], 'wb') as handler:
        handler.write(image_data)

def get_todos() -> list:
    response = requests.get(os.environ['BACKEND_SERVER_URL'], headers={"User-Agent": "Mozilla/5.0"})
    decoded_response = response.content.decode("UTF-8")
    todo_list = eval(decoded_response)
    # strip empty lines
    return [item for item in todo_list if item.strip()]