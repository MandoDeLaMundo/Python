from flask_app import app
from flask import render_template, request, redirect
from flask_app.models.user import User

@app.route('/')
@app.route("/users")
def users():
    users = User.get_all()
    print (users)
    return render_template("read_all.html", all_users = users)

@app.route("/users/<int:id>")
def one_user(id):
    data = { "id": id }
    user = User.get_one(data)
    print (user)
    return render_template("read_one.html", user = user)

@app.route("/users/edit/<int:id>")
def edit_user(id):
    data = { "id": id }
    user = User.get_one(data)
    print (user)
    return render_template("edit.html", user = user)


@app.route('/users/new')
def newUser():
    return render_template('create.html')



@app.route('/create_user', methods = ["POST"])
def create_user():
    user_id = User.save(request.form)
    return redirect (f'/users/{user_id}')

@app.route("/users/update", methods = ["POST"])
def update_user():
    User.update_user(request.form)
    user_id = request.form["id"]
    return redirect(f'/users/{user_id}')

@app.route("/users/<int:id>/delete")
def delete_user(id):
    User.delete_user({ "id": id })
    return redirect('/users')

