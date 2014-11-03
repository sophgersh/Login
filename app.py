from flask import flash, Flask, g, render_template, session, redirect, url_for, escape, request
#from flask.ext.pymongo import PyMongo

import mongo

app = Flask(__name__)
app.secret_key = 'a'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/home')
def home():
    print "here"
    if 'username' in session:
        return render_template('home.html',username = escape(session['username']))
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



if __name__ == '__main__':
    app.debug = True
    app.run()
