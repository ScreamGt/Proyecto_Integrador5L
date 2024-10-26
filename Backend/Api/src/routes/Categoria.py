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
def get_catgoria():
    token = request.args.get('token')
    if ValidarToken.validar_token(token):
        try:
            nombre = request.args.get('nombre')
            if not nombre:  # Comprobar si el nombre está vacío
                return jsonify({'message': 'El nombre es requerido'}), 400 
            categorias = CategoriaModel.get_categoria(nombre)
            # Si no se encuentran categorias, puedes retornar un mensaje específico
            if not categorias:
                return jsonify({'message': 'No se encontraron categoriaas'}), 404
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
            nombre = request.form.get('nombre')
            estado = request.form.get('estado', "activo")  # Valor por defecto

            success = CategoriaModel.add_categoria(nombre, estado)

            # Mensaje para mirar si fue exitoso los cambios en la BD
            if success :  
                return jsonify({'message': 'Categoria agregado exitosamente'})
            else:
                return jsonify({'message': "Ninguna categoria Agregada"}), 404
        
        except Exception as ex:
            return jsonify({'message': str(ex)}), 500
    else:
        return jsonify({'message': "token no valido"}), 500


#Ruta para eliminar una categoria de la BD
@main.route('/delete', methods=['POST'])
def delete_categoria():
    token = request.args.get('token')
    if ValidarToken.validar_token(token) == "administrador":
        try:
            # Recibir datos desde el formulario HTTP POST
            nombre = request.form.get('nombre')
            success = CategoriaModel.delete_categoria(nombre)

            # Mensaje para mirar si fue exitoso los cambios en la BD
            if success:  
                return jsonify({'message': 'Categoria Eliminada'})
            else:
                return jsonify({'message': "Ninguna categoria eliminada"}), 404
        
        except Exception as ex:
            return jsonify({'message': str(ex)}), 500
    else:
        return jsonify({'message': "token no valido"}), 500