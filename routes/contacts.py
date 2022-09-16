from flask import Blueprint, render_template

contacts = Blueprint('contacts', __name__)

@contacts.route('/')
def home():
    return render_template("index.html")

@contacts.route('/new')
def add_contact():
    return "Guardando un nuevo estudiante"

@contacts.route('/update')
def update():
    return "Actualizando un nuevo estudiante"

@contacts.route('/delete')
def delete():
    return "Eliminando un estudiante"