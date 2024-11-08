from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from configs.config import DB_URL, DB_NAME

# Create a new client and connect to the server
client = MongoClient(DB_URL, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

db = client.get_database(DB_NAME)