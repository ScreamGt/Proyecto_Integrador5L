from flask import Blueprint , jsonify, request
from models.LoteModel import LoteModel
from routes import ValidarToken

main = Blueprint('lote_blueprint', __name__)

# Ruta para traer todos los lotes
@main.route('/getAll')
def get_lotes():
    token = request.args.get('token')
    if ValidarToken.validar_token(token):
        try:
            lotes = LoteModel.get_lotes()
            return jsonify(lotes)
        except Exception as ex:
            return jsonify({'message' : str(ex)}) , 500
    else:
        return jsonify({'message': "token no valido"}), 500

# Ruta para traer a proveedores por su nombre
@main.route('/getOne', methods=['GET'])
def get_lote():
    token = request.args.get('token')
    if ValidarToken.validar_token(token):
        try:
            nombre = request.args.get('nombre')
            estado_lote = request.args.get()
            if not nombre:  # Comprobar si el nombre está vacío
                return jsonify({'message': 'Ingresa el nombre del producto o el estado del lote'}), 400 
            lotes = LoteModel.get_lote(nombre, estado_lote)
            # Si no se encuentran lotes, puedes retornar un mensaje específico
            if not lotes:
                return jsonify({'message': 'No se encontraron lotes'}), 404
            return jsonify(lotes)
        except Exception as ex:
            return jsonify({'message': str(ex)}), 500
    else:
        return jsonify({'message': "token no valido"}), 500


#Ruta para agregar un proveedor a la BD 
@main.route('/add', methods=['POST'])
def add_proveedor():
    token = request.args.get('token')
    if ValidarToken.validar_token(token) == "administrador":
        try:
            # Recibir datos desde el formulario HTTP
            nombre = request.form.get('nombre')
            telefono = request.form.get('telefono')
            direccion = request.form.get('direccion')

            success = LoteModel.add_proveedor(nombre, telefono, direccion, "activo")

            # Mensaje para mirar si fue exitoso los cambios en la BD
            if success :  
                return jsonify({'status': 'succesfull'})
            else:
                return jsonify({'status': "Ningun Proveedor Agregado"}), 404
        except Exception as ex:
            return jsonify({'status': str(ex)}), 500
    else:
        return jsonify({'status': "token no valido"})

#Ruta para actualizar un Proveedor
@main.route('/update', methods=['PUT'])
def update_proveedor():
    token = request.args.get('token')
    if ValidarToken.validar_token(token) == "administrador":
        try:
            # Recibir datos desde el formulario HTTP POST
            id_lote = request.args.get('id_lote')
            fecha_llegada = request.args.get('fecha_llegada')
            peso = request.args.get('peso')
            precio = request.args.get('precio')
            success = LoteModel.update_lote(id_lote, fecha_llegada, peso,precio)

            # Mensaje para mirar si fue exitoso los cambios en la BD
            if success :  
                return jsonify({'message': 'Lote actualizado exitosamente'}),200
            else:
                return jsonify({'message': "Ningun Lote actualizado"}), 500
        
        except Exception as ex:
            return jsonify({'message': str(ex)}), 500
    else:
        return jsonify({'message': "token no valido"}), 500

#Ruta para eliminar un lote de la BD
@main.route('/delete', methods=['PUT'])
def delete_lote():
    token = request.args.get('token')
    if ValidarToken.validar_token(token) == "administrador":
        try:
            # Recibir datos desde el formulario HTTP POST
            id_lote = request.args.get('id_lote')
            success = LoteModel.delete_lote(id_lote)

            # Mensaje para mirar si fue exitoso los cambios en la BD
            if success:  
                return jsonify({'message': 'Lote Eliminado'})
            else:
                return jsonify({'message': "Ningun Lote eliminado"}), 404
        
        except Exception as ex:
            return jsonify({'message': str(ex)}), 500
    else:
        return jsonify({'message': "token no valido"}), 500