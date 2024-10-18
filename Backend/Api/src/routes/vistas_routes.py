from flask import Blueprint , jsonify, render_template , request
from models.EmpleadoModel import EmpleadoModel
from models.entities.Empleado import Empleado

Vistas = Blueprint('vistas_routes', __name__)

@Vistas.route('/')
def index():
    return render_template("index.html")

@Vistas.route('/Login')
def Login():
    return render_template("auth-signin.html")

@Vistas.route('/addTransacciones')
def addTransacciones():
    return render_template("nueva-transaccion.html")

@Vistas.route('/Proveedores')
def proveedores():
    return render_template("view_proveedores.html")

@Vistas.route('/addProveedores')
def addProveedores():
    return render_template("nuevo-proveedor.html")

@Vistas.route('/Productos')
def productos():
    return render_template("view_productos.html")

@Vistas.route('/addProductos')
def addProductos():
    return render_template("nuevo-producto.html")

@Vistas.route('/Lote')
def lote():
    return render_template("view_lote.html")

@Vistas.route('/addLote')
def addLote():
    return render_template("nuevo-lote.html")

@Vistas.route('/Empleado')
def empleado():
    return render_template("view_empleado.html")

@Vistas.route('/addEmpleado')
def addEmpleado():
    return render_template("nueva-transaccion.html")