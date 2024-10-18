from flask import Blueprint , jsonify, render_template , request
from models.EmpleadoModel import EmpleadoModel
from models.entities.Empleado import Empleado

Vistas = Blueprint('vistas_routes', __name__)

@Vistas.route('/')
def index():
    return render_template("form.html")

@Vistas.route('/Login')
def Login():
    return render_template("auth-signin.html")

@Vistas.route('/Login')
def Log_out():
    return render_template("auth-signin.html")