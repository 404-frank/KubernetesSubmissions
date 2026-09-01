import os
from datetime import datetime
import requests
IMG_URL = "/usr/app/static/sharedfiles/temp_image.png"

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
