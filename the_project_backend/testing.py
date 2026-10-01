from pymongo import MongoClient
import json
from datetime import datetime
import os

MONGODB_HOST = os.environ.get('MONGODB_HOSTNAME', 'localhost')
MONGODB_PORT = int(os.environ.get('MONGODB_PORT', '9999'))
MONGODB_USERNAME = os.environ.get('MONGODB_USERNAME', '')
MONGODB_PASSWORD = os.environ.get('MONGODB_PASSWORD', '')




uri = f"mongodb://{MONGODB_USERNAME}:{MONGODB_PASSWORD}@{MONGODB_HOST}:{MONGODB_PORT}/"
client = MongoClient(uri)

def get_connection(database: str, collection: str):
    database = client.get_database(database)
    return database.get_collection(collection)


try:
    todo_collection = get_connection("mooc", "todo")

    todo1 = { "id": 1, "title": "put the milk outside too",  "entry_date" : 1746164700}
    todo2 = { "id": 2, "title": "put something else outside",  "entry_date" : 1746164800}
    todo3 = { "id": 3, "title": "put something else inside",  "entry_date" : 1746164800}
    # query_filter = { "id": 2 }
    # update_operation = { '$set' :  { 'title' : 'look how nice!' } }
    result = todo_collection.update_one({ "id": 2 }, { '$set' :  { 'entry_date' : datetime(1967, 3, 12, 0, 0, 0) } })
    print(f"result: {result}")

    for t in [todo1, todo2, todo3]:
        result = todo_collection.insert_one(t)
        print(f"result: {result}")


    query = { "id": 2 }
    todo = todo_collection.find_one(query)

    print(json.dumps(todo, indent=4, default=str))

    client.close()

except Exception as e:
    raise Exception("Unable to find the document due to the following error: ", e)

