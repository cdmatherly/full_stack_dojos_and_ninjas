from flask import render_template, redirect, request
from flask_app import app
from flask_app.models.ninja import Ninja

@app.route('/ninja/create')
def create():
    Ninja.create_ninja()
    return render_template('ninjas.html')
