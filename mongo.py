import pymongo
from pymongo import Connection



#---- run this the first time ------#
def setup():
    conn = Connection()
    db = conn['uncommon']

    print db.collection_names()
    res = db.people.find({},{'_id':False})
       
    
    users = db.users
    post_id = users.insert(user)
    users.find_one()


def addperson(pdict):
    db.users.insert(pdict)

def addfield(uname, field, data):
    p = db.users.find_one(uname)
    p[field] = data
    
    
#setup()

if __name__ == '__main__':
    conn = Connection()
    db = conn.test_database
    people = db.people
    dict = {"fname":"Sophie","lname":"Gershon"}
    people.insert(dict)
    peeps = people.find({"lname":"Gershon"}) 
    # >> gives you a list 
    for p in peeps:
        print p

"""
 people = db.people
 
 to insert
     people.insert(dict)
        
 to update:
     person = people.find_one({"food":"ham"})
     person["food"] = "eggs"
     people.save(person)

 to remove:
     for person in people.find():
        people.remove(person)

 people.find(dict) --> returns a list of people with the dict qualities 
"""

    
