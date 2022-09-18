import re
from flask import Blueprint, render_template, request, redirect, url_for
from models.contact import Contact
from utils.db import db

contacts = Blueprint('contacts', __name__)

#RUTA RAIZ DE LA API
@contacts.route('/')
def index():
    contacts = Contact.query.all()
    return render_template("index.html", contacts=contacts)

#RUTA PARA AGREGAR NUEVOS ESTUDIANTES
@contacts.route('/new', methods=['POST'])
def add_contact():
    cedula=request.form['cedula']
    fullname=request.form['fullname']
    lastname=request.form['lastname']
    age=request.form['age']
    email=request.form['email']
    genero=request.form['genero']

    new_contact = Contact(cedula, fullname, lastname, age, email, genero)

    db.session.add(new_contact)
    db.session.commit()

    return redirect(url_for('contacts.index'))

#RUTA PARA EDITAR INFORMACION DE ESTUDIANTES AGREGADOS
@contacts.route('/update')
def update():
    return "Actualizando un nuevo estudiante"

#RUTA PARA ELIMINAR ESTUDIANTES
@contacts.route('/delete/<id>')
def delete(id):
    contact = Contact.query.get(id)
    db.session.delete(contact)
    db.session.commit()

    return redirect(url_for('contacts.index'))