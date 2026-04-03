from pymongo import MongoClient
import os

client = MongoClient(os.getenv("MONGO_URL"))
db = client["Hackniche"]

events_collection = db["events"]
menu_collection = db["Menu"]
menu_items_collection = db["Menuitem"]