# -*- coding: utf-8 -*-

from pymongo import MongoClient
import urllib.parse

username = urllib.parse.quote_plus('rightcloud')
password = urllib.parse.quote_plus('H89lBgAg')

print(username)
print(password)

mongoClient = MongoClient('mongodb://%s:%s@10.68.6.3:27017' % (username, password))
print(mongoClient)

rightcloud = mongoClient["rightcloud"]

users = rightcloud["users"]

print(users.find_one({'name':'smith'}))

mydict = {"name": "Google", "alexa": "1", "url": "https://www.google.com"}

x = users.insert_one(mydict)

print(x.inserted_id)

mylist = [
  { "name": "Taobao", "alexa": "100", "url": "https://www.taobao.com" },
  { "name": "QQ", "alexa": "101", "url": "https://www.qq.com" },
  { "name": "Facebook", "alexa": "10", "url": "https://www.facebook.com" },
  { "name": "知乎", "alexa": "103", "url": "https://www.zhihu.com" },
  { "name": "Github", "alexa": "109", "url": "https://www.github.com" }
]

x = users.insert_many(mylist)

# 输出插入的所有文档对应的 _id 值
print(x.inserted_ids)

predictions = rightcloud["predictions"]
print(predictions)

predictions.find_one({}, {})
