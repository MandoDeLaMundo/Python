from flask_app import app
from flask import render_template, request, redirect, session, flash
from flask_app.models import login
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt(app)


@app.route('/')
def login_page():
    if "user_id" in session:
        return redirect("/success")
    return render_template("index.html")


@app.route('/success')
def welcome():
    if "user_id" not in session:
        return redirect('/')
    data = {
        "id" : session["user_id"]
    }
    user = login.Login.get_one(data)
    return render_template("success.html", user = user)


@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')



@app.route('/register', methods=['post'])
def register():
    # validate the form here ...
    if not login.Login.validate_register(request.form):
        return redirect('/')
    # create the hash
    pw_hash = bcrypt.generate_password_hash(request.form['password'])
    # put the pw_hash into the data dictionary
    data = {
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "email": request.form['email'],
        "password" : pw_hash
    }
    # Call the save @classmethod on User
    user_id = login.Login.save(data)
    # store user id into session
    session['user_id'] = user_id
    return redirect('/success')


@app.route('/login', methods=['POST'])
def user_login():
    # see if the username provided exists in the database
    data = { "email" : request.form["email"] }
    user_in_db = login.Login.get_by_email(data)
    # user is not registered in the db
    if not user_in_db:
        flash("Invalid Email/Password", "login")
        return redirect("/")
    if not bcrypt.check_password_hash(user_in_db.password, request.form['password']):
        # if we get False after checking the password
        flash("Invalid Email/Password", "login")
        return redirect('/')
    # if the passwords matched, we set the user_id into session
    session['user_id'] = user_in_db.id
    # never render on a post!!!
    return redirect("/success")

