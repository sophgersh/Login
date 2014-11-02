from flask import flash, Flask, g, redirect, render_template, request
#import db

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/user')
def user():
    return render_template('user.html', d={'user':username})


@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/register')
def register():
    return render_template('register.html')



if __name__ == '__main__':
    app.debug = True
    app.run()
