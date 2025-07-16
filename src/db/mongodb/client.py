from core.settings import Settings
from pymongo import MongoClient
from pymongo.server_api import ServerApi

settings = Settings()

client = MongoClient(settings.MONGODB_URI)

db = client[settings.MONGODB_DATABASE]
invoice_log_collection = db["invoice_log"]
