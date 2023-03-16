from flask import render_template, redirect, request
from flask_app import app
from flask_app.models.ninja import Ninja
from flask_app.models.dojo import Dojo

@app.route('/ninjas')
def add():
    all_dojos = Dojo.show_all()
    return render_template('new_ninja.html', all_dojos = all_dojos)

@app.route('/ninjas/create', methods=['POST'])
def create():
    Ninja.create_ninja(request.form)
    return redirect(f"/dojos/{request.form['dojo_id']}")
