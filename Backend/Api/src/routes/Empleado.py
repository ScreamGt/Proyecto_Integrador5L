from flask import Blueprint , jsonify, render_template , request
from models.EmpleadoModel import EmpleadoModel
from models.entities.Empleado import Empleado

main = Blueprint('empleado_blueprint', __name__)

@main.route('/')
def get_empleados():
    try:
        empleados = EmpleadoModel.get_empleados()
        return jsonify(empleados)
    except Exception as ex:
        return jsonify({'message' : str(ex)}) , 500
    
@main.route('/<cedula>')
def get_empleado(cedula):
    try:
        empleado = EmpleadoModel.get_empleado(cedula)
        if empleado != None:
            return jsonify(empleado)
        else:
            return jsonify(None)
    except Exception as ex:
        return jsonify({'message' : str(ex)}) , 500
    
@main.route('/add', methods=['POST'])
def add_empleado():
    try:
        # Recibir datos desde el formulario HTTP POST
        cedula_empleado = request.form.get('cedula_empleado')
        nombre_completo = request.form.get('nombre_completo')
        correo = request.form.get('correo')
        rol = request.form.get('rol')

        print(cedula_empleado, nombre_completo, correo, rol)

        # Crear el empleado con los datos recibidos
        empleado = Empleado(cedula_empleado, nombre_completo, correo, rol)

        # Aquí puedes agregar la lógica para guardar el empleado en la BD
        EmpleadoModel.add_empleado(empleado)  

        return jsonify({'message': 'Empleado agregado exitosamente'}), 200
    
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500
