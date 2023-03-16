from flask import render_template, redirect, request
from flask_app import app
from flask_app.models.dojo import Dojo

@app.route("/")
def redirect_to_dojos():
    return redirect('/dojos')

@app.route("/dojos")
def index():
    all_dojos = Dojo.show_all()

    return render_template("dojos.html", all_dojos=all_dojos)