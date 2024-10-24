from flask import Blueprint , jsonify, request
from models.ProveedoresModel import ProveedoresModel
from models.entities.Proveedores import Proveedores

main = Blueprint('proveedores_blueprint', __name__)

# Ruta para traer todos los proveedores
@main.route('/getAll')
def get_proveedores():
    try:
        proveedores = ProveedoresModel.get_proveedores()
        return jsonify(proveedores)
    except Exception as ex:
        return jsonify({'message' : str(ex)}) , 500

#Ruta para traer un proveedor por su nombre
@main.route('/getOne')
def get_proveedor():
    try:
        nombre = request.form.get('nombre')
        proveedor = ProveedoresModel.get_proveedor(nombre)
        if proveedor != None:
            return jsonify(proveedor)
        else:
            return jsonify(None)
    except Exception as ex:
        return jsonify({'message' : str(ex)}) , 500

#Ruta para agregar un proveedor a la BD 
@main.route('/add', methods=['POST'])
def add_proveedor():
    try:
        # Recibir datos desde el formulario HTTP
        telefono = request.form.get('telefono')
        nombre = request.form.get('nombre')
        direccion = request.form.get('direccion')

        # Crear el proveedor con los datos recibidos
        proveedor = Proveedores(telefono, nombre, direccion)
        affected_rows = ProveedoresModel.add_proveedor(proveedor)

        # Mensaje para mirar si fue exitoso los cambios en la BD
        if affected_rows == 1:  
            return jsonify({'message': 'Proveedor agregado exitosamente'}),
        else:
            return jsonify({'message': "Ningun Proveedor Agregado"}), 404
    
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500

#Ruta para actualizar un Proveedor
@main.route('/update', methods=['PUT'])
def update_proveedor():
    try:
        # Recibir datos desde el formulario HTTP POST
        telefono = request.form.get('telefono')
        nombre = request.form.get('nombre')
        direccion = request.form.get('direccion')

        # Crear el proveedor con los datos recibidos
        proveedor = Proveedores(telefono, nombre, direccion)
        affected_rows = ProveedoresModel.update_proveedor(proveedor)

        # Mensaje para mirar si fue exitoso los cambios en la BD
        if affected_rows == 1:  
            return jsonify({'message': 'Proveedor actualizado exitosamente'}),
        else:
            return jsonify({'message': "Ningun Proveedor actualizado"}), 500
    
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500

#Ruta para eliminar un proveedor de la BD
@main.route('/delete', methods=['DELETE'])
def delete_proveedor():
    try:
        # Recibir datos desde el formulario HTTP POST
        proveedor = request.form.get('nombre')
        affected_rows = ProveedoresModel.delete_proveedor(proveedor)

        # Mensaje para mirar si fue exitoso los cambios en la BD
        if affected_rows == 1:  
            return jsonify({'message': 'Proveedor Eliminado'}), 
        else:
            return jsonify({'message': "Ningun Proveedor eliminado"}), 404
    
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500