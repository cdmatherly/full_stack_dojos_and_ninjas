from flask import render_template, redirect, request
from flask_app import app
from flask_app.models.dojo import Dojo

@app.route("/")
def index():
    return redirect('/dojos')

@app.route("/dojos")
def main():
    all_dojos = Dojo.show_all()

    return render_template("dojos.html", all_dojos=all_dojos)

@app.route('/dojos/create', methods=['POST'])
def create_dojo():
    Dojo.save(request.form)
    return redirect('/')

@app.route("/dojos/<int:dojo_id>")
def show_one_dojo(dojo_id):
    one_dojo = Dojo.get_one(dojo_id)
    one_dojo_dict = {
        'id' : one_dojo.id,
        'name' : one_dojo.name,
        'created_at' : one_dojo.created_at,
        'updated_at' : one_dojo.updated_at
    }
    dojo_result = Dojo.show_dojos_with_ninjas(one_dojo_dict)
    # print (f"!!!!!!!!!!!!!!!!!!!!!!!!!!DOJO RESULT>>>>>>>>>>>>>>{dojo_result.ninjas}")
    return render_template('one_dojo.html', dojo = dojo_result)