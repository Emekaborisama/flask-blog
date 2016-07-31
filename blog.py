# Blog using flask, hosted on AWS
# blog.py - controller

# imports
from flask import Flask, render_template, request, session, flash, redirect, \
url_for, g
import sqlite3

# configuration

DATABASE = 'blog.db'
USERNAME = 'admin'
PASSWORD = 'admin'
SECRET_KEY = '\xf3\x86\xd9q\xac\x12\xef\x00z\xab\xe6\xb1\x0e\x99\x81\xdaX\xadE\xe1\x8f\x86\x80\xa8'



app = Flask(__name__)

# pulls in app configuration by looking for uppercase variables
app.config.from_object(__name__)

# fuction used for connecting to the DATABASE
def connect_db():
    return sqlite3.connect(app.config['DATABASE'])

@app.route('/', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != app.config['USERNAME'] or \
        request.form['password'] != app.config['PASSWORD']:
            error = 'Invalid Credentials. Please Try again.'
        else:
            session['logged_in'] = True
            return redirect(url_for('main'))
    return render_template('login.html', error = error)

@app.route('/main')
def main():
    return render_template('main.html')


if __name__ == '__main__':
    app.run(debug=True)
