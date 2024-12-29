import os
from dotenv import load_dotenv
from motor.motor_asyncio import AsyncIOMotorClient

# Load environment variables from .env file
load_dotenv()

MONGO_URI ="mongodb+srv://kashyap:kashyap14kp@cluster0.jp9de.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
DATABASE_NAME = "test_db"  # Replace with your database name
COLLECTION_NAME = "test_collection"  # Replace with your collection name



client = AsyncIOMotorClient(MONGO_URI)
db = client[DATABASE_NAME]
collection = db[COLLECTION_NAME]
