import os
from dotenv import load_dotenv
from motor.motor_asyncio import AsyncIOMotorClient

# Load environment variables from .env file
load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")
DATABASE_NAME = "test_db"  # Replace with your database name
COLLECTION_NAME = "test_collection"  # Replace with your collection name

# Print MongoDB URI
print("MongoDB URI:", MONGO_URI)

client = AsyncIOMotorClient(MONGO_URI)
db = client[DATABASE_NAME]
collection = db[COLLECTION_NAME]
