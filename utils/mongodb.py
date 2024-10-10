from pymongo.mongo_client import MongoClient
from configs.config import DB_URL, DB_NAME
from certifi import where

# Create a new client and connect to the server
client = MongoClient(DB_URL)

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("MongoDB Connected!")
except Exception as e:
    print(e)

db = client.get_database(DB_NAME)