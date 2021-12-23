from pymongo import MongoClient

conn = MongoClient('localhost', 27017)
db = conn["db_products"]
col = db["product"]
