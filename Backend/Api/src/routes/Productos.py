from flask import Blueprint , jsonify, request
from models.ProductosModel import ProductosModel
from routes import ValidarToken

main = Blueprint('productos_blueprint', __name__)

# Ruta para traer todos los producto
@main.route('/getAll')
def get_productos():
    token = request.args.get('token')
    if ValidarToken.validar_token(token):
        try:
            productos = ProductosModel.get_productos()
            return jsonify(productos)
        except Exception as ex:
            return jsonify({'message' : str(ex)}) , 500
    else:
        return jsonify({'message': "token no valido"}), 500

#Ruta para traer un producto por su nombre
@main.route('/getOne_name', methods=['GET'])
def get_producto_nombre():
    token = request.args.get('token')
    if ValidarToken.validar_token(token):
        try:
            nombre = request.args.get('nombre')
            productos = ProductosModel.get_producto_nombre(nombre)

            if productos != None:
                return jsonify(productos)
            else:
                return jsonify(None)
        except Exception as ex:
            return jsonify({'message' : str(ex)}) , 500
        
#Ruta para traer un producto por su categoria
@main.route('/getOne_categ', methods=['GET'])
def get_producto_categoria():
    token = request.args.get('token')
    if ValidarToken.validar_token(token):
        try:
            nombre_categoria = request.args.get('nombre_categoria')
            productos = ProductosModel.get_producto_categoria(nombre_categoria)

            if productos != None:
                return jsonify(productos)
            else:
                return jsonify(None)
        except Exception as ex:
            return jsonify({'message' : str(ex)}) , 500

#Ruta para agregar un producto a la BD 
@main.route('/add', methods=['POST'])
def add_producto():
    token = request.args.get('token')
    if ValidarToken.validar_token(token):
        try:
            # Recibir datos desde el formulario HTTP
            codigo_producto = request.form.get('codigo_producto')
            nombre = request.form.get('nombre')
            precio_libra = request.form.get('precio_libra')
            nombre_categoria = request.form.get('nombre_categoria')

            # Crear el producto con los datos recibidos
            Sucess = ProductosModel.add_producto(codigo_producto, nombre, precio_libra, 'activo', nombre_categoria)

            # Mensaje para mirar si fue exitoso los cambios en la BD
            if Sucess:  
                return jsonify({'message': 'Producto agregado exitosamente'})
            else:
                return jsonify({'message': "Ningun Producto Agregado"}), 404
    
        except Exception as ex:
            return jsonify({'message': str(ex)}), 500

#Ruta para actualizar un Producto
@main.route('/update', methods=['PUT'])
def update_producto():
    try:
        # Recibir datos desde el formulario HTTP POST
        nombre = request.args.get('nombre')
        precio_libra = request.args.get('precio_libra')
        nombre_categoria = request.args.get('nombre_categoria')

        # Crear el producto con los datos recibidos
        Sucess = ProductosModel.update_producto(nombre, precio_libra, nombre_categoria)

        # Mensaje para mirar si fue exitoso los cambios en la BD
        if Sucess:  
            return jsonify({'message': 'Producto actualizado exitosamente'})
        else:
            return jsonify({'message': "Ningun Producto actualizado"}), 500
    
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500

#Ruta para eliminar un producto de la BD
@main.route('/delete', methods=['PUT'])
def delete_proveedor():
    try:
        # Recibir datos desde el formulario HTTP POST
        nombre = request.args.get('nombre')
        affected_rows = ProductosModel.delete_producto(nombre)

        # Mensaje para mirar si fue exitoso los cambios en la BD
        if affected_rows == 1:  
            return jsonify({'message': 'Producto Eliminado'})
        else:
            return jsonify({'message': "Ningun Producto eliminado"}), 404
    
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500