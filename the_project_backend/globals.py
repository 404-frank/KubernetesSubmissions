from pymongo import MongoClient
import json
from datetime import datetime
import os

MONGODB_HOST = os.environ.get('MONGODB_HOSTNAME', 'localhost')
MONGODB_PORT = int(os.environ.get('MONGODB_PORT', '9999'))
MONGODB_USERNAME = os.environ.get('MONGODB_USERNAME', '')
MONGODB_PASSWORD = os.environ.get('MONGODB_PASSWORD', '')

URI = f"mongodb://{MONGODB_USERNAME}:{MONGODB_PASSWORD}@{MONGODB_HOST}:{MONGODB_PORT}/"

def get_connection(database: str, collection: str):
    database = client.get_database(database)
    return database.get_collection(collection)

def add_todo(todo_title : str):
    print("in add_todo") 
    client = MongoClient(URI)
    database = client.get_database("mooc")
    todo_collection = database.get_collection("todo")
    todo = { "id": 1, "title": todo_title,  "entry_date" : datetime.now()}
    result = todo_collection.insert_one(todo)
    print(f"result: {result}")
    # client.close()

# returns a list of todo's, a list of strings    
def get_todos() -> list:
    print("in get_todos")
    client = MongoClient(URI)
    database = client.get_database("mooc")
    todo_collection = database.get_collection("todo")
    todo_list = todo_collection.find()
    print(f"todo_list: {todo_list}")
    # client.close()
    return [t['title'] for t in todo_list]

