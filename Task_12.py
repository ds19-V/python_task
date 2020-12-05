#Create a JSON of all object types and import the JSON into a SQL Database
import  json
a={
    "Name":"DEEPASREE",
    "Age":19,
    "city":"chennai",
    "grade": None,
    "result": True,
    "marks1":{"SE":100,"DS":95},
    "marks2":[80,98,90],
    "avg": 92.6
}
b=json.dumps(a)
print(b)
print(json.dumps((1,2,3)))
print(json.dumps(list(range(5))))

from pymongo import MongoClient
myclient=MongoClient("mongodb://localhost:27017/")
db=myclient["ABC"]
Collection=db["data"]
with open('D:\\Python Internship\\task12\\data.json') as f:
    file_data=json.load(f)
if isinstance(file_data,list):
    Collection.insert_many(file_data)
else:
    Collection.insert_one(file_data)

