# coding: utf8
import os
import sqlite3
from flask import Flask, render_template, url_for, request, redirect, \
    session, abort, flash
from model import User

app = Flask(__name__)

app.config["DATABASE"] = 'database.db'


def connect_db():
    """Connects to the specific database."""
    db = sqlite3.connect(app.config['DATABASE'])
    return db


def init_db():
    with app.app_context():
        db = connect_db()
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login/', methods=['GET', 'POST'])
def user_login():
    return render_template('user_login.html')


@app.route('/regist/', methods=['GET', 'POST'])
def user_regist():
    if request.method == 'POST':
        print(request.form)
        user = User()
        user.name = request.form["user_name"]
        user.pwd = request.form["user_pwd"]
        user.email = request.form['user_email']
        user.age = request.form['user_age']
        user.birthday = request.form['user_birthday']
        user.face = request.form['user_face']
        print(user.name)
        return redirect(url_for("user_login", username=user.name))
    return render_template('user_regist.html')


if __name__ == '__main__':
    app.run(debug=True)

    25
