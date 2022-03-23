from flask_app import app
from flask import render_template, request, redirect
from flask_app.models.dojo import Dojo
from flask_app.models.ninja import Ninja

@app.route('/')
@app.route('/dojos')
def dojo():
    dojos = Dojo.get_all()
    return render_template("dojos.html", dojos = dojos)


@app.route("/dojos/<int:id>")
def show_dojo(id):
    data = { "id": id }
    dojo = Dojo.get_one_dojo(data)
    return render_template("show_dojo.html", dojo = dojo)

@app.route('/ninja')
def ninjas():
    dojo = Dojo.get_all()
    return render_template("new_ninja.html", dojos = dojo)



@app.route('/create_dojo', methods = ["post"])
def create_dojo():
    dojo_id = Dojo.save(request.form)
    return redirect ('/dojos')


@app.route('/create_ninja', methods = ["post"])
def create_ninja():
    Ninja.save(request.form)
    dojo_id = request.form["dojo_id"]
    return redirect (f'/dojos/{dojo_id}')