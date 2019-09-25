import pymongo
from bson import ObjectId

db = pymongo.MongoClient('mongodb://test:test@127.0.0.1/test').test


