from flask import Flask
from routes.contacts import contacts
from flask_sqlalchemy import SQLAlchemy
from config import DATABASE_CONNECTION_URI

app = Flask(__name__)

#Aqui se realiza la conexion con la bases de datos local - en este caso de MySQL
#La estructura de la conexion es la siguiente: 'mysql://root:(contrasena)@(Nombre del servidor)/(Nombre de la base de datos)'
#P.D No pongas los parentesis!!!!!

app.secret_key = "secret key"
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_CONNECTION_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

SQLAlchemy(app)

app.register_blueprint(contacts)