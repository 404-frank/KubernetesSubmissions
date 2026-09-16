import os
from datetime import datetime
import requests
IMG_URL = "/usr/app/static/sharedfiles/temp_image.png"
# IMG_URL = "/home/frank/Applications/KubernetesPlayground/KubernetesSubmissions/the_project/static/temp_image.png"
TODO_BACKEND_URL = 'http://localhost:3001/todos'

def get_image_url():
    if image_too_old(IMG_URL):
        # get new one
        retrieve_new_image()
    return "/static/sharedfiles/temp_image.png"


def image_too_old(imageFileName: str) -> bool:
    if os.path.isfile(imageFileName):
        mtime = datetime.fromtimestamp(os.path.getmtime(imageFileName))
        time_diff_seconds = int((datetime.now() - mtime).total_seconds())
        # print(time_diff_seconds)
        return time_diff_seconds > 600
    return True

def retrieve_new_image():
    url = 'https://picsum.photos/1200'
    response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
    image_data = response.content
    with open(IMG_URL, 'wb') as handler:
        handler.write(image_data)

def get_todos() -> list:
    response = requests.get(TODO_BACKEND_URL, headers={"User-Agent": "Mozilla/5.0"})
    decoded_response = response.content.decode("UTF-8")
    todo_list = eval(decoded_response)
    # strip empty lines
    return [item for item in todo_list if item.strip()]