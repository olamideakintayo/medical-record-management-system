import os
from pymongo import MongoClient
from dotenv import load_dotenv
import mongomock

load_dotenv()
MONGO_URI = os.getenv("MONGO_URI")

if os.getenv("TESTING", "0") == "1":
    client = mongomock.MongoClient()
else:
    client = MongoClient(MONGO_URI)

db = client["MedicalCluster"]
