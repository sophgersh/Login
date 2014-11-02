import pymongo
from pymongo import MongoClient



#---- run this the first time ------#
def setup():
    client = MongoClient()
    db = client.test_database
    collection = db.test_collection
    user = {"fname":"Sophie","lname":"Gershon"}
    users = db.users
    post_id = users.insert(user)
    users.find_one()
    
setup()

def addperson(dict):
    
