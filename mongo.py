import pymongo
from pymongo import Connection

conn = Connection()
db = conn["uncommon"]
users = db.users

def new_user(udict):
    pwcheck = (udict['pw'] == udict['rpw'])
    un = udict['uname'] 
    uncheck = users.find_one({'uname':un}) == None
    s = ""
    if uncheck == False:
        s = "That username has already been used"
    elif pwcheck == False:
        s =  "Passwords do not match"
    else:
        addperson(udict)
    print s
    return s

def check_pword(uname,pw):
    rpw = getAttribute("pw",uname)
    if rpw == None:
        return "Username does not exist"
    if rpw == pw:
        return ""
    else:
        return "Wrong password"

def addperson(pdict):
    db.users.insert(pdict)

def addfield(uname, field, data):
    #p = users.find_one({"fname":fname})
    #p[field] = data
    #users.save(p)
    users.update({"uname":uname},{'$set':{field:data}})

    
def getAttribute(field, uname):
    ret = users.find_one({'uname':uname})
    if ret == None:
        return None
    ret = ret[field]
    #print(ret)
    return ret
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

    
