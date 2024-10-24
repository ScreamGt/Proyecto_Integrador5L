from flask import Blueprint , jsonify, request
from models.EmpleadoModel import EmpleadoModel
from models.entities.Empleado import Empleado

main = Blueprint('empleado_blueprint', __name__)

# Ruta para traer todos los empleados
@main.route('/getAll')
def get_empleados():
    try:
        empleados = EmpleadoModel.get_empleados()
        return jsonify(empleados)
    except Exception as ex:
        return jsonify({'message' : str(ex)}) , 500

#Ruta para traer un empleado por su cedula
@main.route('/getOne')
def get_empleado():
    try:
        cedula_empleado = request.form.get('cedula_empleado')
        empleado = EmpleadoModel.get_empleado(cedula_empleado)
        if empleado != None:
            return jsonify(empleado)
        else:
            return jsonify(None)
    except Exception as ex:
        return jsonify({'message' : str(ex)}) , 500

#Ruta para agregar un empleado a la BD 
@main.route('/add', methods=['POST'])
def add_empleado():
    try:
        # Recibir datos desde el formulario HTTP POST 
        cedula_empleado = request.form.get('cedula_empleado')
        nombre_completo = request.form.get('nombre_completo')
        correo = request.form.get('correo')
        rol = request.form.get('rol')

        # Crear el empleado con los datos recibidos
        empleado = Empleado(cedula_empleado, nombre_completo, correo, rol)
        affected_rows = EmpleadoModel.add_empleado(empleado)

        # Mensaje para mirar si fue exitoso los cambios en la BD
        if affected_rows == 1:  
            return jsonify({'message': 'Empleado agregado exitosamente'}),
        else:
            return jsonify({'message': "Ningun Empleado Agregado"}), 404
    
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500

#Ruta para actualizar un empleado
@main.route('/update', methods=['PUT'])
def update_empleado():
    try:
        # Recibir datos desde el formulario HTTP POST
        cedula_empleado = request.form.get('cedula_empleado')
        nombre_completo = request.form.get('nombre_completo')
        correo = request.form.get('correo')
        rol = request.form.get('rol')

        # Crear el empleado con los datos recibidos
        empleado = Empleado(cedula_empleado, nombre_completo, correo, rol)
        affected_rows = EmpleadoModel.update_empleado(empleado)

        # Mensaje para mirar si fue exitoso los cambios en la BD
        if affected_rows == 1:  
            return jsonify({'message': 'Empleado actualizado exitosamente'}),
        else:
            return jsonify({'message': "Ningun Empleado actualizado"}), 500
    
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500

#Ruta para eliminar un empleado de la BD
@main.route('/delete', methods=['DELETE'])
def delete_empleado():
    try:
        # Recibir datos desde el formulario HTTP POST
        empleado = request.form.get('cedula_empleado')
        affected_rows = EmpleadoModel.delete_empleado(empleado)

        # Mensaje para mirar si fue exitoso los cambios en la BD
        if affected_rows == 1:  
            return jsonify({'message': 'Empleado Eliminado'}), 
        else:
            return jsonify({'message': "Ningun Empleado eliminado"}), 404
    
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500