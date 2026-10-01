import requests
from pymongo import MongoClient
import json
from datetime import datetime
import os

MONGODB_HOST = os.environ.get('MONGODB_HOSTNAME', 'localhost')
MONGODB_PORT = int(os.environ.get('MONGODB_PORT', '9999'))
MONGODB_USERNAME = os.environ.get('MONGODB_USERNAME', '')
MONGODB_PASSWORD = os.environ.get('MONGODB_PASSWORD', '')
WIKIPEDIA_RANDOM_URL = "https://en.wikipedia.org/wiki/Special:Random/"
MONGODB_URI = f"mongodb://{MONGODB_USERNAME}:{MONGODB_PASSWORD}@{MONGODB_HOST}:{MONGODB_PORT}/"

def get_random_article_url() -> str:
    headers = {"Accept": "application/json", "User-Agent": "frank@frankprins.nl"}
    random_article = requests.get(WIKIPEDIA_RANDOM_URL, allow_redirects=True, headers=headers, timeout=10)
    article_name = random_article.url.split("/")[-1]
    return article_name, f"https://en.wikipedia.org/wiki/{article_name}"

def add_todo(todo_title : str):
    print("in add_todo") 
    client = MongoClient(MONGODB_URI)
    database = client.get_database("mooc")
    todo_collection = database.get_collection("todo")
    todo = { "id": 1, "title": todo_title,  "entry_date" : datetime.now()}
    result = todo_collection.insert_one(todo)
    print(f"result: {result}")
    client.close()

def main():
    print("start automatic todo creation")
    random_article_url = get_random_article_url()
    print(f"new url: [{random_article_url}]")
    todo = f"Visit this Wikipedia article: <a href='{random_article_url[1]}' class='underline text-[#693434]' target='_blank'>{random_article_url[0]}</a>"
    print(f"going to add todo: [{todo}]")
    add_todo(todo)
    print(f"added todo")

if __name__ == '__main__':
    main()