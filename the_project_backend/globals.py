from pymongo import MongoClient
import json
from datetime import datetime
import os

MONGODB_HOST = os.environ.get('MONGODB_HOSTNAME', 'localhost')
MONGODB_PORT = int(os.environ.get('MONGODB_PORT', '27017'))
MONGODB_USERNAME = os.environ.get('MONGODB_USERNAME', 'admin')
MONGODB_PASSWORD = os.environ.get('MONGODB_PASSWORD', 'admin')

URI = f"mongodb://{MONGODB_USERNAME}:{MONGODB_PASSWORD}@{MONGODB_HOST}:{MONGODB_PORT}/"

def get_connection(database: str, collection: str):
    database = client.get_database(database)
    return database.get_collection(collection)

def add_todo(todo_title : str):
    print("in add_todo") 
    client = MongoClient(URI)
    database = client.get_database("mooc")
    todo_collection = database.get_collection("todo")
    next_id = get_next_id(todo_collection)
    todo = { "id": next_id, "title": todo_title, "entry_date": datetime.now(), "done": False }
    result = todo_collection.insert_one(todo)
    print(f"result: {result}")
    #client.close()

def get_next_id(col):
    num_records = col.count_documents({})
    max_id = 0
    if num_records > 0:
        counter = col.find({}, {'_id' : 1, 'id': 1}).sort({'id': -1}).limit(1)
        max_id = int(counter.next()['id'])
    max_id += 1
    return max_id

def set_todo_done(todo_id: int):
    print("in set_todo_done")
    client = MongoClient(URI)
    database = client.get_database("mooc")
    todo_collection = database.get_collection("todo")
    query_filter = {'id': int(todo_id)}
    update_operation = { '$set' : { 'done' : True }}
    result = todo_collection.update_one(query_filter, update_operation)

# returns a list of todo's, a list of strings    
def get_todos() -> list:
    print("in get_todos")
    client = MongoClient(URI)
    database = client.get_database("mooc")
    todo_collection = database.get_collection("todo")
    todo_list = todo_collection.find()
    list_to_return = [(t['id'], t['done'], t['title']) for t in todo_list]
    # print(f"list_to_return: {list_to_return}")
    return list_to_return
    #client.close()

def check_database_health() -> bool:
    try:
        client = MongoClient(URI)
        client.admin.command('ping')
        return True
    except ConnectionFailure:
        print("Server not available")
        return False