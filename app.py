from flask import flash, Flask, g, render_template, session, redirect, url_for, escape, request
#from flask.ext.pymongo import PyMongo

import mongo

app = Flask(__name__)
app.secret_key = 'a'

@app.route('/')
def index():
    return redirect('/home')

@app.route('/home')
def home():
    # print "here"
    if 'username' in session:
        username = escape(session['username'])
        fname = mongo.getAttribute(username, "fname")
        return render_template('home.html', fname = fname, username = username)
        #return render_template('home.html', mongo.get_user())
    return render_template('home.html')

@app.route('/user', methods=['POST'])
def user():
    #print("user!");
    if request.method=="POST":
        print request.form['uname']
        newuser = {}
        newuser['uname'] = request.form['uname']
        newuser['fname'] = request.form['fname']
        newuser['lname'] = request.form['lname']
        newuser['pw'] = request.form['pw']
        newuser['rpw'] = request.form['rpw']
        valid_msg = mongo.new_user(newuser)
        if valid_msg == '':
            session['username'] = request.form['uname']
            return redirect('/home')
        else:
            flash(valid_msg)
            return redirect('/register')

@app.route('/login')
def login():
    
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    return render_template('login.html')
@app.route('/register')
def register():
    
    return render_template('register.html')

@app.route('/verify', methods=['POST'])
def verify():
    if request.method=="POST":
        uname = request.form['uname']
        pw = request.form['pw']
        valid_msg = mongo.check_pword(uname,pw)
        if valid_msg == '':
            session['username'] = uname
            return redirect('/home')
        else:
            flash(valid_msg)
            return redirect('/login')

@app.route('/personal', methods=['GET','POST'])
def personal():    
    username = escape(session['username'])

    if request.method=="POST":
        submit = request.form['submit']
        if submit == 'name':
            mongo.addfield(username,"fname",request.form["fname"])
            mongo.addfield(username,"lname",request.form["lname"])          
        mongo.addfield(username,submit,request.form[submit])
    return render_template('personal.html', udict=mongo.getUser(username))

@app.route('/name')
def name():
    username = escape(session['username'])
    return render_template('personal.html', udict=mongo.getUser(username),change = "change" )
    
@app.route('/age')
def age():
    username = escape(session['username'])
    return render_template('personal.html', udict = mongo.getUser(username),changeage = "change" )

@app.route('/gpa')
def gpa():
    username = escape(session['username'])

    return render_template('personal.html', udict = mongo.getUser(username),changegpa = "change" )

@app.route('/colleges')
def colleges():
    pass



if __name__ == '__main__':
    app.debug = True
    app.run()
