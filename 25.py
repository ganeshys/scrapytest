# 测试mongodb的连接
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.blog_database
collection = db.blog