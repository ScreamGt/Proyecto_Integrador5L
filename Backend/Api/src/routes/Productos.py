from flask import Blueprint , jsonify, request
from models.ProductosModel import ProductosModel
from models.entities.Productos import Productos

main = Blueprint('productos_blueprint', __name__)

# Ruta para traer todos los producto
@main.route('/getAll')
def get_productos():
    try:
        productos = ProductosModel.get_productos()
        return jsonify(productos)
    except Exception as ex:
        return jsonify({'message' : str(ex)}) , 500

#Ruta para traer un producto por su nombre
@main.route('/getOne')
def get_producto():
    try:
        nombre = request.form.get('nombre')
        producto = ProductosModel.get_producto(nombre)
        if producto != None:
            return jsonify(producto)
        else:
            return jsonify(None)
    except Exception as ex:
        return jsonify({'message' : str(ex)}) , 500

#Ruta para agregar un producto a la BD 
@main.route('/add', methods=['POST'])
def add_producto():
    try:
        # Recibir datos desde el formulario HTTP
        codigo_producto = request.form.get('codigo_producto')
        nombre = request.form.get('nombre')
        direccion = request.form.get('direccion')

        # Crear el producto con los datos recibidos
        producto = Productos(codigo_producto, nombre, direccion)
        affected_rows = ProductosModel.add_proveedor(producto)

        # Mensaje para mirar si fue exitoso los cambios en la BD
        if affected_rows == 1:  
            return jsonify({'message': 'Producto agregado exitosamente'}),
        else:
            return jsonify({'message': "Ningun Producto Agregado"}), 404
    
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500

#Ruta para actualizar un Producto
@main.route('/update', methods=['PUT'])
def update_producto():
    try:
        # Recibir datos desde el formulario HTTP POST
        telefono = request.form.get('telefono')
        nombre = request.form.get('nombre')
        direccion = request.form.get('direccion')

        # Crear el producto con los datos recibidos
        producto = Productos(telefono, nombre, direccion)
        affected_rows = ProductosModel.update_producto(producto)

        # Mensaje para mirar si fue exitoso los cambios en la BD
        if affected_rows == 1:  
            return jsonify({'message': 'Producto actualizado exitosamente'}),
        else:
            return jsonify({'message': "Ningun Producto actualizado"}), 500
    
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500

#Ruta para eliminar un proveedor de la BD
@main.route('/delete', methods=['DELETE'])
def delete_proveedor():
    try:
        # Recibir datos desde el formulario HTTP POST
        proveedor = request.form.get('nombre')
        affected_rows = ProductosModel.delete_proveedor(proveedor)

        # Mensaje para mirar si fue exitoso los cambios en la BD
        if affected_rows == 1:  
            return jsonify({'message': 'Proveedor Eliminado'}), 
        else:
            return jsonify({'message': "Ningun Proveedor eliminado"}), 404
    
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500