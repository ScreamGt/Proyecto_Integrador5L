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

# Ruta para traer a proveedores por su nombre
@main.route('/getOne', methods=['GET'])
def get_proveedor():
    try:
        nombre = request.args.get('nombre')
        if not nombre:  # Comprobar si el nombre está vacío
            return jsonify({'message': 'El nombre es requerido'}), 400 
        proveedores = ProveedoresModel.get_proveedor(nombre)
        # Si no se encuentran proveedores, puedes retornar un mensaje específico
        if not proveedores:
            return jsonify({'message': 'No se encontraron proveedores'}), 404
        return jsonify(proveedores)
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500


#Ruta para agregar un proveedor a la BD 
@main.route('/add', methods=['POST'])
def add_proveedor():
    try:
        # Recibir datos desde el formulario HTTP
        nombre = request.form.get('nombre')
        telefono = request.form.get('telefono')
        direccion = request.form.get('direccion')
        estado = request.form.get('estado', "activo")  # Valor por defecto

        success = ProveedoresModel.add_proveedor(nombre, telefono, direccion, estado)

        # Mensaje para mirar si fue exitoso los cambios en la BD
        if success :  
            return jsonify({'message': 'Proveedor agregado exitosamente'})
        else:
            return jsonify({'message': "Ningun Proveedor Agregado"}), 404
    
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500

#Ruta para actualizar un Proveedor
@main.route('/update', methods=['POST'])
def update_proveedor():
    try:
        # Recibir datos desde el formulario HTTP POST
        telefono = request.form.get('telefono')
        nombre = request.form.get('nombre')
        direccion = request.form.get('direccion')

        success = ProveedoresModel.update_proveedor(nombre, telefono, direccion)

        # Mensaje para mirar si fue exitoso los cambios en la BD
        if success :  
            return jsonify({'message': 'Proveedor actualizado exitosamente'}),200
        else:
            return jsonify({'message': "Ningun Proveedor actualizado"}), 500
    
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500

#Ruta para eliminar un proveedor de la BD
@main.route('/delete', methods=['POST'])
def delete_proveedor():
    try:
        # Recibir datos desde el formulario HTTP POST
        nombre = request.form.get('nombre')
        estado = request.form.get('estado', "inactivo")  # Valor por defecto
        success = ProveedoresModel.delete_proveedor(nombre, estado)

        # Mensaje para mirar si fue exitoso los cambios en la BD
        if success:  
            return jsonify({'message': 'Proveedor Eliminado'}), 
        else:
            return jsonify({'message': "Ningun Proveedor eliminado"}), 404
    
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500