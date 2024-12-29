import os
from dotenv import load_dotenv
from motor.motor_asyncio import AsyncIOMotorClient

# Load environment variables from .env file
load_dotenv()

# Fetch MongoDB URI, Database Name, and Collection Name from .env
MONGO_URI = os.getenv("MONGO_URI")
DATABASE_NAME = os.getenv("DATABASE_NAME", "test_db")  # Default to "test_db" if not set in .env
COLLECTION_NAME = os.getenv("COLLECTION_NAME", "test_collection")  # Default to "test_collection"

# Initialize MongoDB client
client = AsyncIOMotorClient(MONGO_URI)
db = client[DATABASE_NAME]
collection = db[COLLECTION_NAME]
