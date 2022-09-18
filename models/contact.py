from utils.db import db

class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cedula = db.Column(db.String(10))
    fullname = db.Column(db.String(100))
    lastname = db.Column(db.String(100))
    age = db.Column(db.String(3))
    email = db.Column(db.String(100))
    genero = db.Column(db.String(1))

    def __init__(self, cedula, fullname, lastname, age, email, genero):
        self.cedula = cedula
        self.fullname = fullname
        self.lastname = lastname
        self.age = age
        self.email = email
        self.genero = genero
