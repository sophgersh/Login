from flask import flash, Flask, g, redirect, render_template, request
#from flask.ext.pymongo import PyMongo

import mongo

app = Flask(__name__)
app.secret_key = 'a'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/home', methods=['POST'])
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
        print("hey!");
        if valid_msg == '':
            return render_template('home.html', d=newuser)
        else:
            flash(valid_msg)
            return redirect('/register')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/register')
def register():
    return render_template('register.html')



if __name__ == '__main__':
    app.debug = True
    app.run()
