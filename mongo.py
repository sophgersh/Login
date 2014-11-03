import pymongo
from pymongo import Connection

conn = Connection()
db = conn["uncommon"]
users = db.users

def new_user(udict):
    pwcheck = (udict['pw'] == udict['rpw'])
    uncheck = users.find({'uname':udict['uname']}) == 0
    s = ""
    if uncheck == False:
        s = "The username has already been used"
    elif pwcheck == False:
        s =  "Passwords do not match"
    else:
        addperson(udict)
    print s
    return s
        

def addperson(pdict):
    db.users.insert(pdict)

def addfield(fname, field, data):
    #p = users.find_one({"fname":fname})
    #p[field] = data
    #users.save(p)
    users.update({"fname":fname},{'$set':{field:data}})

#setup()

if __name__ == '__main__':
    #db = conn.test_database
    dict = {"fname":"Loras","lname":"Tyrell"}
    #people.insert(dict)
    addfield("Loras","uname","knightofflowers")

    #users.remove({"fname":{"$exists":False}})
    
    peeps = users.find({},{'_id':False}) 
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

    
