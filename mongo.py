import pymongo, csv
from pymongo import Connection


conn = Connection()
db = conn["uncommon"]
users = db.users
colleges = db.colleges

def new_user(udict):
    pwcheck = (udict['pw'] == udict['rpw'])
    uname = udict['uname'] 
    uncheck = users.find_one({'uname':uname}) == None
    s = ""
    if uncheck == False:
        s = "That username has already been used"
    elif len(pw) >= 5 and len(pw) <= 20:
        s= "Password must be between 5 and 20 characters"
    elif pwcheck == False:
        s =  "Passwords do not match"
    else:
        addperson(udict)
    print s
    return s

def check_pword(uname,pw):
    rpw = getAttribute(uname,"pw")
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

    
def getAttribute(uname, field):
    ret = users.find_one({'uname':uname, field:{'$exists':True}})
    if ret == None:
        return None
    ret = ret.get(field)
    #print(ret)
    return ret

def getUser(uname):
    return users.find_one({'uname':uname})
    
def createColleges():
    cols = csv.DictReader(open("colleges.csv"))
    for c in cols:
        colleges.insert(c)

def collegeLookup(dict):
    cols = colleges.find(dict)
    
        

if __name__ == '__main__':

    #colleges.remove()
    #createColleges()
    '''  
    peeps = users.find({},{'_id':False}) 
    for p in peeps:
        print p
    print 
    peeps = colleges.find({},{'_id':False}) 
    for p in peeps:
        print p
    '''
    print getUser('sophgersh')
        
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
 users.remove({"fname":{"$exists":False}})
"""

    
