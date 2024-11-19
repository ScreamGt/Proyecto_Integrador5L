from flask import Blueprint , jsonify, request
from models.CategoriaModel import CategoriaModel
from routes import ValidarToken

main = Blueprint('categoria_blueprint', __name__)

# Ruta para traer todos las categorias
@main.route('/getAll')
def get_categorias():
    token = request.args.get('token')
    if ValidarToken.validar_token(token):
        try:
            categorias = CategoriaModel.get_categorias()
            return jsonify(categorias)
        except Exception as ex:
            return jsonify({'message' : str(ex)}) , 500
    else:
        return jsonify({'message': "token no valido"}), 500

# Ruta para traer a categoria por su nombre
@main.route('/getOne', methods=['GET'])
def get_categoria():
    token = request.args.get('token')
    if ValidarToken.validar_token(token):
        try:
            categoria = request.args.get('categoria')
            categorias = CategoriaModel.get_categoria(categoria)
            
            if not categorias:
                return jsonify({'message': 'No se encontraron categorias'}), 404
            return jsonify(categorias)
        except Exception as ex:
            return jsonify({'message': str(ex)}), 500
    else:
        return jsonify({'message': "token no valido"}), 500

#Ruta para agregar una categoria a la BD 
@main.route('/add', methods=['POST'])
def add_categoria():
    token = request.args.get('token')
    if ValidarToken.validar_token(token) == "administrador":
        try:
            # Recibir datos desde el formulario HTTP
            categoria = request.form.get('categoria')

            success = CategoriaModel.add_categoria(categoria, "activo" )

            # Mensaje para mirar si fue exitoso los cambios en la BD
            if success :  
                return jsonify({'message': 'Categoria agregado exitosamente'})
            else:
                return jsonify({'message': "Ninguna categoria Agregada"}), 404
        except Exception as ex:
            return jsonify({'message': str(ex)}), 500
    else:
        return jsonify({'status': "token no valido"})

#Ruta para eliminar un categoria de la BD
@main.route('/delete', methods=['PUT'])
def delete_categoria():
    token = request.args.get('token')
    if ValidarToken.validar_token(token) == "administrador":
        try:
            # Recibir datos desde el formulario HTTP POST
            categoria = request.args.get('categoria')
            success = CategoriaModel.delete_categoria(categoria)
            
            # Mensaje para mirar si fue exitoso los cambios en la BD
            if success:  
                return jsonify({'message': 'Categoria Eliminada'})
            else:
                return jsonify({'message': "Ninguna categoria eliminada"}), 404
        except Exception as ex:
            return jsonify({'message': str(ex)}), 500
    else:
        return jsonify({'status': "token no valido"})